"""
Simple example code to communicate with Power BI REST API. Hope it helps.
"""
import requests

# Configuration goes here:
RESOURCE = "https://analysis.windows.net/powerbi/api"  # Don't change that.
APPLICATION_ID = "8b6ca47c-dc6e-41a8-8073-e97a333d40a4"  # The ID of the application in Active Directory
APPLICATION_SECRET = "5y_q:_XppEG6BJ]uX44UXLABJOo7/ScS"  # A valid key for that application in Active Directory

USER_ID = "pbicdg@konectaperu.onmicrosoft.com"  # A user that has access to PowerBI and the application
USER_PASSWORD = "Pb1_K0c_Cdg"  # The password for that user

def get_access_token(application_id=APPLICATION_ID, application_secret=APPLICATION_SECRET, user_id=USER_ID, user_password=USER_PASSWORD):
    data = {
        'grant_type': 'password',
        'scope': 'openid',
        'resource': "https://analysis.windows.net/powerbi/api",
        'client_id': application_id,
        'client_secret': application_secret,
        'username': user_id,
        'password': user_password
    }
    token = requests.post("https://login.microsoftonline.com/common/oauth2/token", data=data)
    assert token.status_code == 200, "Fail to retrieve token: {}".format(token.text)
    #print("Got access token: ")
    #print(token.json())
    return token.json()['access_token']

def make_headers(application_id=APPLICATION_ID, application_secret=APPLICATION_SECRET, user_id=USER_ID, user_password=USER_PASSWORD):
    return {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': "Bearer {}".format(get_access_token(application_id, application_secret, user_id, user_password))
    }


def get_embed_token_report(application_id=APPLICATION_ID, application_secret=APPLICATION_SECRET, user_id=USER_ID, user_password=USER_PASSWORD, group_id=None, report_id=None):
    endpoint = "https://api.powerbi.com/v1.0/myorg/groups/{}/reports/{}/GenerateToken".format(group_id, report_id)
    headers = make_headers(application_id, application_secret, user_id, user_password)
    res = requests.post(endpoint, headers=headers, json={"accessLevel": "View"})
    return res.json()['token']


def get_groups(application_id=APPLICATION_ID, application_secret=APPLICATION_SECRET, user_id=USER_ID, user_password=USER_PASSWORD):
    endpoint = "https://api.powerbi.com/v1.0/myorg/groups"
    headers = make_headers(application_id, application_secret, user_id, user_password)
    return requests.get(endpoint, headers=headers).json()


def get_dashboards(application_id=APPLICATION_ID, application_secret=APPLICATION_SECRET, user_id=USER_ID, user_password=USER_PASSWORD, group_id=None):
    endpoint = "https://api.powerbi.com/v1.0/myorg/groups/{}/dashboards".format(group_id)
    headers = make_headers(application_id, application_secret, user_id, user_password)
    return requests.get(endpoint, headers=headers).json()


def get_reports(application_id=APPLICATION_ID, application_secret=APPLICATION_SECRET, user_id=USER_ID, user_password=USER_PASSWORD, group_id=None):
    endpoint = "https://api.powerbi.com/v1.0/myorg/groups/{}/reports".format(group_id)
    headers = make_headers(application_id, application_secret, user_id, user_password)
    return requests.get(endpoint, headers=headers).json()


def get_datasets(application_id=APPLICATION_ID, application_secret=APPLICATION_SECRET, user_id=USER_ID, user_password=USER_PASSWORD, group_id=None):
    endpoint = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets".format(group_id)
    headers = make_headers(application_id, application_secret, user_id, user_password)
    return requests.get(endpoint, headers=headers).json()


def get_refreshes(application_id=APPLICATION_ID, application_secret=APPLICATION_SECRET, user_id=USER_ID, user_password=USER_PASSWORD, dataset_id=None):
    endpoint = "https://api.powerbi.com/v1.0/myorg/datasets/{}/refreshes".format(dataset_id)
    headers = make_headers(application_id, application_secret, user_id, user_password)
    return requests.get(endpoint, headers=headers).json()


def get_refreshschedule(application_id=APPLICATION_ID, application_secret=APPLICATION_SECRET, user_id=USER_ID, user_password=USER_PASSWORD, dataset_id=None):
    endpoint = "https://api.powerbi.com/v1.0/myorg/datasets/{}/refreshSchedule".format(dataset_id)
    headers = make_headers(application_id, application_secret, user_id, user_password)
    return requests.get(endpoint, headers=headers).json()