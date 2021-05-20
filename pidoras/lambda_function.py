import json
import boto3
from covidscraper import scrapeGlobalCase
def lambda_handler(event, context):

    s3 = boto3.resource('s3')
    print("[INFO] Request COVID-19 data...")
    update_covid_cases = scrapeGlobalCase()
    BUCKET_NAME = "covidscraper"
    DATE = f"{update_covid_cases['date']}"
    OUTPUT_NAME = f"dataKeyTest{DATE}.json"
    OUTPUT_BODY = json.dumps(update_covid_cases)
    print(f"[INFO] Saving Data to S3 {BUCKET_NAME} Bucket...")
    s3.Bucket(BUCKET_NAME).put_object(Key=OUTPUT_NAME, Body=OUTPUT_BODY)
    print(f"[INFO] Job done at {DATE}")