# AWS Recognition with Scraping

This project implements an automated system for processing and analyzing images from MyAuto.ge using AWS services. The system scrapes images from the website, processes them through AWS Rekognition, and stores the results in a structured format.

## Project Overview

The system is designed to automatically collect images from MyAuto.ge, analyze them using AWS Rekognition for object and scene detection, and store the results in a structured format for further analysis.

## Project Structure

![alt text](<Requirements Management Plan - Lambda Handler For Myauto Pictures (1).jpg>)

## Features

- Automated image scraping from MyAuto.ge
- AWS Rekognition integration for image analysis
- Structured data storage and processing
- Lambda-based serverless architecture
- Automated workflow management

## Prerequisites

- Python 3.8 or higher
- AWS Account with appropriate permissions
- Required AWS services:
  - AWS Lambda
  - AWS Rekognition
  - AWS S3

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd AWSRecognitionWithScrapping
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure AWS credentials:
   ```bash
   aws configure
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Project Structure

```
AWSRecognitionWithScrapping/
├── src/
│   ├── lambda/
│   │   ├── handler.py
│   │   └── requirements.txt
│   └── scraper/
│       ├── scraper.py
│       └── requirements.txt
├── README.md
└── requirements.txt
```

## Usage

1. Create S3 Bucket:
   ```bash
   # Create a new S3 bucket for storing car images
   aws s3 mb s3://rekognition-car-images --region us-west-2
   ```

2. Set up Lambda Function:
   - Create a new Lambda function in AWS Console
   - Set the runtime to Python 3.9
   - Upload the `lambda_handler.py` code
   - Configure the following settings:
     - Memory: 256 MB
     - Timeout: 5 minutes
     - Environment variables:
       - DYNAMO_DB_TABLE: rekognitionAnalyzeDB
       - REKOGNITION_SNS_TOPIC_ARN: [Your SNS Topic ARN]
   - Add S3 trigger:
     - Source bucket: [Your S3 Bucket Name]
     - Event types: All object create events
     - Prefix: (leave empty to process all images)
     - Suffix: .jpg

3. Configure IAM Role:
   - Create a new IAM role for Lambda
   - Attach the following policies:
     - AWSLambdaBasicExecutionRole
     - AmazonRekognitionFullAccess
     - AmazonS3ReadOnlyAccess
     - AmazonDynamoDBFullAccess
   - Update the `configuration.json` with the role ARN:
     ```json
     {
         "lambdaRole": "arn:aws:iam::[YOUR_ACCOUNT_ID]:role/[YOUR_ROLE_NAME]",
         "region": "us-west-2",
         "dynamoDBtable": "rekognitionAnalyzeDB",
         "s3BucketName": "[Your S3 Bucket Name]"
     }
     ```

4. Run the Scraper:
   ```bash
   python Scrapping/myauto_scrapper.py --s3-bucket rekognition-car-images --pages 1 --output-dir car_images
   ```

5. Monitor the Process:
   - Check S3 bucket for uploaded images
   - Monitor Lambda function logs in CloudWatch
   - View results in DynamoDB table
   - Check SNS notifications for completion status

## Contact

Project Link: [https://github.com/ninikvinikadze02/AWSRecognitionWithScrapping]