import os
from azure.identity import AzureCliCredential
from azure.mgmt.storage import StorageManagementClient

credential = AzureCliCredential()
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
RESOURCE_GROUP_NAME = "testRgCreateBySDK"
LOCATION = "centralus"
storage_client = StorageManagementClient(credential, subscription_id)
STORAGE_ACCOUNT_NAME = "pythonstoragetechcon98"

CONTAINER_NAME = "blob-container-01-bysdk"
container = storage_client.blob_containers.create(
    RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME, CONTAINER_NAME, {}
)
print(f"Provisioned blob container {container.name}")