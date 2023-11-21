# Use the official MinIO image as the base image
FROM minio/minio

# Set environment variables for MinIO access and secret keys
ENV MINIO_ROOT_USER=myaccesskey
ENV MINIO_ROOT_PASSWORD=mysecretkey

      
# Expose the default MinIO port
EXPOSE 9000

# Set the default command to start MinIO server
CMD ["server", "--address", "127.0.0.1:9000", "/data"]