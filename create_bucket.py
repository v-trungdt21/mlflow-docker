import os

from minio import Minio
from minio.error import InvalidResponseError

accessID = os.environ.get("MINIO_ROOT_USER")
accessSecret = os.environ.get("MINIO_ROOT_PASSWORD")
minioUrl = os.environ.get("MLFLOW_S3_ENDPOINT_URL")
bucketName = os.environ.get("BUCKET_NAME")

if accessID == None:
    print(
        "[!] MINIO_ROOT_USER environemnt variable is empty! run 'source .env' to load it from the .env file"
    )
    exit(1)

if accessSecret == None:
    print(
        "[!] MINIO_ROOT_PASSWORD environemnt variable is empty! run 'source .env' to load it from the .env file"
    )
    exit(1)

if minioUrl == None:
    print(
        "[!] MLFLOW_S3_ENDPOINT_URL environemnt variable is empty! run 'source .env' to load it from the .env file"
    )
    exit(1)


if bucketName == None:
    print(
        "[!] BUCKET_NAME environemnt variable is empty! run 'source .env' to load it from the .env file"
    )
    exit(1)

minioUrlHostWithPort = minioUrl.split("//")[1]
print("[*] minio url: ", minioUrlHostWithPort)

s3Client = Minio(
    minioUrlHostWithPort, access_key=accessID, secret_key=accessSecret, secure=False
)

s3Client.make_bucket(bucketName)
