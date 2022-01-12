from azure.identity import AzureCliCredential
from azure.keyvault.secrets import SecretClient

d_credentials = AzureCliCredential()

secret_client = SecretClient(
    vault_url="https://testingkvcx.vault.azure.net/", credential=d_credentials
)
my_secret = secret_client.get_secret(name="testsecretval")

print(my_secret.value)