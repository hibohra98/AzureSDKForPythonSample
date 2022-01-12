"""
AzureCLICredentials will use the Logged In CLI session to authenticate to Azure
"""

import os
from azure.identity import AzureCliCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters, Sku

credential = AzureCliCredential()
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
RESOURCE_GROUP_NAME = "testRgCreateBySDK"
LOCATION = "eastus"
storage_client = StorageManagementClient(credential, subscription_id)
STORAGE_ACCOUNT_NAME = "pythonstoragetechcon98"
response = storage_client.storage_accounts.begin_create(
    RESOURCE_GROUP_NAME,
    STORAGE_ACCOUNT_NAME,
    StorageAccountCreateParameters(
        sku=Sku(name="Standard_LRS"),
        kind="Storage",
        location="westus",
        enable_https_traffic_only=True,
    ),
)
storage_account = response.result()
print(
    f"Storage account {storage_account.name} provision state is {storage_account.provisioning_state}"
)
