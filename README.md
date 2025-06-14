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
  - AWS EventBridge

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
├── tests/
├── .env.example
├── README.md
└── requirements.txt
```

## Usage

### Run Scrapper code :
'''
python Scrapping/myauto_scrapper.py --s3-bucket rekognition-car-images --pages 1 --output-dir car_images
'''
1. Deploy the Lambda function

2. Configure EventBridge rules

3. Monitor the process

## Contact

Project Link: [https://github.com/ninikvinikadze02/AWSRecognitionWithScrapping]