"""Cloud / infrastructure dependencies.

One function per dependency: boto3, google-cloud-storage, azure-storage-blob,
kubernetes, docker.
"""

import boto3
from google.cloud import storage as gcs
from azure.storage.blob import BlobServiceClient
import kubernetes
import docker


def s3_client(region: str = "us-east-1"):
    """boto3: build an S3 client."""
    return boto3.client("s3", region_name=region)


def gcs_client():
    """google-cloud-storage: build a GCS client (credentials lazy)."""
    # Construction may require credentials at call time; reference the class.
    return gcs.Client


def azure_blob_service(conn_str: str = "UseDevelopmentStorage=true"):
    """azure-storage-blob: build a BlobServiceClient from a connection string."""
    return BlobServiceClient.from_connection_string(conn_str)


def kube_core_api_class():
    """kubernetes: reference the CoreV1Api client class."""
    return kubernetes.client.CoreV1Api


def docker_client_from_env():
    """docker: build a Docker client from the environment."""
    return docker.from_env
