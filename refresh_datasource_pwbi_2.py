import adal
from pypowerbi.client import PowerBIClient

# you might need to change these, but i doubt it
authority_url = 'https://login.windows.net/common'
resource_url = 'https://analysis.windows.net/powerbi/api'
api_url = 'https://api.powerbi.com'

# change these to your credentials
client_id = '086b2f7a-e2a9-4b4a-aa65-f0bb14457924'
username = 'pbicdg@konectaperu.onmicrosoft.com'
password = 'Pb1_K0c_Cdg'

# first you need to authenticate using adal
context = adal.AuthenticationContext(authority=authority_url,
                                     validate_authority=True,
                                     api_version=None)

# get your authentication token
token = context.acquire_token_with_username_password(resource=resource_url,
                                                     client_id=client_id,
                                                     username=username,
                                                     password=password)

# create your powerbi api client
client = PowerBIClient(api_url, token)

# Refresh the desired dataset (dataset and group IDs can be taken from the browser URL)
client.datasets.refresh_dataset(dataset_id='1498a3ef-2292-4ab5-a931-958008d3268f',
                                notify_option='MailOnCompletion',
                                group_id='c57c794d-7b25-4750-8496-c4c014187853')