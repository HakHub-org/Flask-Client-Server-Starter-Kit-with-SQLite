"""
Third-Party Services Integration
"""

import os
import boto3

# Email Service Configuration
smtp_server = os.getenv("SMTP_SERVER")
smtp_username = os.getenv("SMTP_USERNAME")
smtp_password = os.getenv("SMTP_PASSWORD")

# Cloud Storage Service Configuration
cloud_provider = os.getenv("CLOUD_PROVIDER")
cloud_access_key = os.getenv("CLOUD_ACCESS_KEY")
cloud_secret_key = os.getenv("CLOUD_SECRET_KEY")
cloud_bucket_name = os.getenv("CLOUD_BUCKET_NAME")

def upload_to_cloud(file_path):
    """
    Upload a file to the cloud storage.

    Args:
        file_path (str): Path of the file to upload.
    """
    if cloud_provider == "aws_s3":
        s3 = boto3.client("s3", aws_access_key_id=cloud_access_key, aws_secret_access_key=cloud_secret_key)
        s3.upload_file(file_path, cloud_bucket_name, file_path)
