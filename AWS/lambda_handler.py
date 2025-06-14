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
    for record in event['Records']:
        objectExtension = record['s3']['object']['key'].split('.')[-1].lower()
        if objectExtension in config['supportedFormats']:
            bucket_name = record['s3']['bucket']['name']
            object_key = urllib.parse.unquote_plus(record['s3']['object']['key'])
            put_labels_in_db(get_image_labels(bucket_name, object_key), object_key, bucket_name)
    return
