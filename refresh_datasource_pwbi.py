import adal
import requests
authority_url = 'https://login.windows.net/common'
resource_url = 'https://analysis.windows.net/powerbi/api'
client_id = '086b2f7a-e2a9-4b4a-aa65-f0bb14457924'
username = 'pbicdg@konectaperu.onmicrosoft.com'
password = 'Pb1_K0c_Cdg'
context = adal.AuthenticationContext(authority=authority_url,
                                     validate_authority=True,
                                     api_version=None)
token = context.acquire_token_with_username_password(resource=resource_url,
                                                     client_id=client_id,
                                                     username=username,
                                                     password=password)
access_token = token.get('accessToken')
refresh_url = 'https://api.powerbi.com/v1.0/myorg/groups/c57c794d-7b25-4750-8496-c4c014187853/datasets/95f6c068-d531-4704-b917-449ad87e860f/refreshes'
header = {'Authorization': f'Bearer {access_token}'}
r = requests.post(url=refresh_url, headers=header)
r.raise_for_status()