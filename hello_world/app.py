import json
import boto3
from botocore.config import Config

# import requests


def lambda_handler(event, context):

    # create the configuration object
    conf = Config(
        region_name='us-east-2',
        signature_version='v4',
        retries={
            'max_attempts': 10,
            'mode': 'standard'
        }
    )

    # create a boto3 s3 client
    s3 = boto3.client('s3', config=conf)

    # create putobjectrequest object
    put_object_request = s3.generate_presigned_post(
        Bucket='test-bucket-360041415327-us-east-2',
        Key='test.txt',
        ExpiresIn=3600
    )
    

    return {
        'statusCode': 200,
        'body': put_object_request['url']
    }