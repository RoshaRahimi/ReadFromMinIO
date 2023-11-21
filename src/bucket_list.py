import boto3

# Set your MinIO server information
endpoint_url = 'http://localhost:9000'  # Replace with your MinIO server URL
access_key = 'minio_access_key'
secret_key = 'minio_secret_key'

# Create an S3 client
s3 = boto3.client('s3', endpoint_url=endpoint_url, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# List buckets
try:
    response = s3.list_buckets()
    print("Buckets:")
    for bucket in response['Buckets']:
        print(f"  {bucket['Name']}")
except Exception as e:
    print(f"Error listing buckets: {e}")
