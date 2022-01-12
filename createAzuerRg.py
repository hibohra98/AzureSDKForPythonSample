from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient

subscription_id = "8b2784e7-dcf8-42c7-b457-241d839c6068"
RESOURCE_GROUP_NAME = "testRgCreateBySDK"
LOCATION = "eastus"
credential = ServicePrincipalCredentials(
    client_id="<Client Id>",
    secret="<Secret>",
    tenant="<Tenant ID>",
)
resource_client = ResourceManagementClient(credential, subscription_id)
response = resource_client.resource_groups.create_or_update(
    RESOURCE_GROUP_NAME, {"location": LOCATION}
)
print(f"Resource Group {response.name} has been created in {response.location}")
