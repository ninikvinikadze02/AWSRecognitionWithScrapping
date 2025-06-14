import json
import os
import urllib
import uuid
import boto3

# Load configurations
with open('configuration.json') as config_file:
    config = json.load(config_file)

def get_image_labels(bucket, key):
    rekognition_client = boto3.client('rekognition', region_name=config['region'])
    response = rekognition_client.detect_labels(
        Image={'S3Object': {
            'Bucket': bucket,
            'Name': key
        }}, MaxLabels=10)
    return response

def make_item(data):
    if isinstance(data, dict):
        return {k: make_item(v) for k, v in data.items()}

    if isinstance(data, list):
        return [make_item(v) for v in data]

    if isinstance(data, float):
        return str(data)

    return data

def put_labels_in_db(data, media_name, media_bucket):
    data.pop('ResponseMetadata', None)
    data['mediaType'] = 'Image'
    data['mediaName'] = media_name
    data['mediaBucket'] = media_bucket
    data['id'] = str(uuid.uuid1())

    dynamodb = boto3.resource('dynamodb', region_name=config['region'])
    table_name = config['dynamoDBtable']
    videos_table = dynamodb.Table(table_name)

    data = make_item(data)
    videos_table.put_item(Item=data)
    return

def start_processing_media(event, context):
    sns_client = boto3.client('sns', region_name=config['region'])
    
    for record in event['Records']:
        objectExtension = record['s3']['object']['key'].split('.')[-1].lower()
        if objectExtension in ['jpeg', 'jpg', 'png', 'mp4']:
            bucket_name = record['s3']['bucket']['name']
            object_key = urllib.parse.unquote_plus(record['s3']['object']['key'])
            
            # Get labels from Rekognition
            labels = get_image_labels(bucket_name, object_key)
            
            # Prepare message for SNS
            message = {
                'bucket': bucket_name,
                'key': object_key,
                'labels': labels
            }
            
            # Publish to SNS topic
            sns_client.publish(
                TopicArn=os.environ['REKOGNITION_SNS_TOPIC_ARN'],
                Message=json.dumps(message)
            )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Processing started successfully')
    }

def handle_label_detection(event, context):
    for record in event['Records']:
        # Parse the SNS message
        sns_message = json.loads(record['Sns']['Message'])
        
        # Extract data from the message
        bucket_name = sns_message['bucket']
        object_key = sns_message['key']
        labels = sns_message['labels']
        
        # Store results in DynamoDB
        put_labels_in_db(labels, object_key, bucket_name)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Labels processed and stored successfully')
    }
