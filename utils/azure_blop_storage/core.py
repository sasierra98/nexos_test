from os import environ
from azure.storage.blob import BlobServiceClient, ContainerClient
import pandas as pd

CONNECTION_STR = environ['CONNECTION_STRING']


class AzureBlobStorage:
    def __init__(self, connection_str: str):
        self.connection_str = connection_str
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_str)

    def validate_container(self, container_name: str):
        container = ContainerClient.from_connection_string(self.connection_str, container_name)
        if container.exists():
            return
        type(self.blob_service_client.create_container(container_name))
        return self.blob_service_client.create_container(container_name)

    def create_container(self, container_name: str):
        return self.validate_container(container_name)

    def upload_file_to_container(
            self,
            container_name: str,
            file_name: str,
            file: pd.DataFrame,
            client_id: int
    ) -> None:
        container = ContainerClient.from_connection_string(self.connection_str, container_name)
        container.upload_blob(name=f'{client_id}/{file_name}.csv', data=file.to_csv(index=False))

    def delete_blob(self, container_name: str, file_name: str, client_id: int):
        container = ContainerClient.from_connection_string(self.connection_str, container_name)
        container.delete_blob(f'{client_id}/{file_name}.csv')