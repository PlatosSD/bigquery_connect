from os import environ
from google.oauth2 import service_account
import pandas as pd
from gcp import get_credentials

def read_bq():
    project_id = environ['NAME_PROJECT']
    print(project_id)
    credentials = get_credentials()

    # read BIGQUERY
    query = '''
    SELECT *  
    FROM DB_NAME.TABLE_NAME
    LIMIT 10    
    '''
    bq_df = pd.read_gbq(
        query, credentials=credentials,  project_id=project_id)
    
    print(bq_df.head())

    return None

read_bq()