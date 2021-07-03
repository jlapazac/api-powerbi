import rest_api as rest_api
import method as method
import connection as connection
import pandas as pd
import time
import pyodbc

conn_str = (
    r'DRIVER={SQL Server Native Client 11.0};'
    r'SERVER=localhost;'
    r'DATABASE=Azure;'
    r'Trusted_Connection=yes;'
)

def get_groups_temp():
    return method.exec_reader(connection.str_ds_pejcb933bdrp_Latam(), 'EXEC PowerBI.uSp_GetGroups')

def get_datasets_temp():
    return method.exec_reader(connection.str_ds_pejcb933bdrp_Latam(), 'EXEC PowerBI.uSp_GetDatasets')

def get_refreshes_temp():
    return method.exec_reader(connection.str_ds_pejcb933bdrp_Latam(), 'EXEC PowerBI.uSp_GetRefreshes')

groups_temp = get_groups_temp()
datasets_temp = get_datasets_temp()
refreshes_temp = get_refreshes_temp()

def set_groups():
    response_groups = rest_api.get_groups()
    groups = pd.DataFrame(response_groups['value'])
    load_groups = (groups[~(groups.isin(groups_temp).all(axis=1))])
    return load_groups

print(set_groups())

    # 
    # for group_index, group_row in groups.iterrows():
    #     print(group_row['id'])
    #     response_datasets = rest_api.get_datasets(group_id = group_row['id'])
    #     datasets = pd.DataFrame(response_datasets['value'])
    #     datasets.info()
    #     print(datasets)

    #     for dataset_index, dataset_row in datasets.iterrows(): 
    #         print(dataset_row['id'])
    #         response_refreshes = rest_api.get_refreshes(dataset_id = dataset_row['id'])
    #         if(len(response_refreshes)==1):
    #             print(response_refreshes['error'])
    #         else:
    #             refreshs = pd.DataFrame(response_refreshes['value'])
    #             refreshs.info()

    #         response_refreshschedule = rest_api.get_refreshschedule(dataset_id = dataset_row['id'])
    #         if(len(response_refreshschedule)==1):
    #             print(response_refreshschedule['error'])
    #         else:
    #             refreshschedule = json_normalize(response_refreshschedule)
    #             refreshschedule.info()
    #             print(refreshschedule)