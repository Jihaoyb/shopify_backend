import boto3
from botocore.exceptions import NoCredentialsError
from app.core.config import settings

# Initialize the S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION
)

def upload_file_to_s3(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket"""
    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, bucket, object_name)
        return True
    except NoCredentialsError:
        return False

def download_file_from_s3(bucket, object_name, file_name=None):
    """Download a file from an S3 bucket"""
    if file_name is None:
        file_name = object_name

    try:
        s3.download_file(bucket, object_name, file_name)
        return True
    except NoCredentialsError:
        return False