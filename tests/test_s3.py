from moto import mock_aws
import boto3
from app.services.s3 import upload_file_to_s3, download_file_from_s3

@mock_aws
def test_upload_file_to_s3():
    # Setup: Create a mock S3 environment
    s3 = boto3.client('s3', region_name='us-east-1')
    s3.create_bucket(Bucket='test-bucket')

    # Test the upload functionality
    result = upload_file_to_s3('testfile.txt', 'test-bucket')
    assert result is True

@mock_aws
def test_download_file_from_s3():
    # Setup: Create a mock S3 environment
    s3 = boto3.client('s3', region_name='us-east-1')
    s3.create_bucket(Bucket='test-bucket')
    s3.put_object(Bucket='test-bucket', Key='testfile.txt', Body=b'Test content')

    # Test the download functionality
    result = download_file_from_s3('test-bucket', 'testfile.txt', 'downloaded_testfile.txt')
    assert result is True
