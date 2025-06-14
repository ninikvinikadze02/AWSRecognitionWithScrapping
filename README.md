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
- Serverless Framework CLI
- Required AWS services:
  - AWS Lambda
  - AWS Rekognition
  - AWS S3
  - AWS SNS
  - AWS DynamoDB

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd AWSRecognitionWithScrapping
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   npm install -g serverless
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

5. Configure serverless deployment:
   - Update `configuration.json` with your AWS account details:
     ```json
     {
         "lambdaRole": "arn:aws:iam::[YOUR_ACCOUNT_ID]:role/[YOUR_ROLE_NAME]",
         "region": "us-west-2",
         "dynamoDBtable": "rekognitionAnalyzeDB",
         "s3BucketName": "[Your S3 Bucket Name]"
     }
     ```

## Deployment

1. Deploy the serverless application:
   ```bash
   serverless deploy
   ```

2. The deployment will create:
   - Lambda functions for image processing and label detection
   - SNS topic for Rekognition notifications
   - DynamoDB table for storing results
   - Required IAM roles and permissions

## Lambda Functions

The application includes two main Lambda functions:

1. `startProcessingMedia`: Triggered by S3 events when new images are uploaded
   - Processes .jpeg, .png, and .mp4 files
   - Initiates AWS Rekognition analysis
   - Sends results to SNS topic

2. `handleLabelDetection`: Triggered by SNS notifications
   - Processes Rekognition results
   - Stores analysis in DynamoDB
   - Handles completion status

## Project Structure

```
AWSRecognitionWithScrapping/
├── AWS/
│   ├── serverless.yml
│   └── handler.py
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

1. Run the Scraper:
   ```bash
   python Scrapping/myauto_scrapper.py --s3-bucket rekognition-car-images --pages 1 --output-dir car_images
   ```

2. Monitor the Process:
   - Check S3 bucket for uploaded images
   - Monitor Lambda function logs in CloudWatch
   - View results in DynamoDB table
   - Check SNS notifications for completion status

## Contact

Project Link: [https://github.com/ninikvinikadze02/AWSRecognitionWithScrapping]