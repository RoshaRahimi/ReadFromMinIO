import boto3
import os

# Set your MinIO server information
endpoint_url = 'http://localhost:9000'  # Replace with your MinIO server URL
access_key = 'minio_access_key'
secret_key = 'minio_secret_key'

file_name = input('input the name of file to download:')
local_path=os.path.join('../data',file_name)
# Set the bucket name and file to upload
bucket_name = input('input the name of bucket that contain the file:')

# Create an S3 client
s3 = boto3.client('s3', endpoint_url=endpoint_url, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# Upload the file
try:
    s3.download_file(bucket_name, file_name, local_path)
    print(f"File '{file_name}' downloaded into '{local_path}' successfully!")
except Exception as e:
    print(f"Error uploading file: {e}")

    # os.path
