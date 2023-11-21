import boto3
import os

# Set your MinIO server information
endpoint_url = 'http://localhost:9000'  # Replace with your MinIO server URL
access_key = 'minio_access_key'
secret_key = 'minio_secret_key'

relative_file_path = input('input the name of file to upload')

# Set the bucket name and file to upload
bucket_name = 'testbucket'
file_path = os.path.join('../data', relative_file_path)

# Create an S3 client
s3 = boto3.client('s3', endpoint_url=endpoint_url, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# Upload the file
try:
    s3.upload_file(file_path, bucket_name, relative_file_path)
    print(f"File '{file_path}' uploaded to '{bucket_name}' successfully with relative path '{relative_file_path}'.")
except Exception as e:
    print(f"Error uploading file: {e}")


    # os.path
