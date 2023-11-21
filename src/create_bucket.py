import boto3

# Set your MinIO server information
endpoint_url = 'http://localhost:9000'  # Replace with your MinIO server URL
access_key = 'minio_access_key'
secret_key = 'minio_secret_key'
bucket_name = input('input a name for the Bucket:')

s3 = boto3.client('s3', endpoint_url = endpoint_url, aws_access_key_id = access_key, aws_secret_access_key = secret_key)

# Create a new bucket
try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully.")
except Exception as e:
    print(f"Error creating bucket: {e}")