from dotenv import load_dotenv
from google.cloud import bigquery
from google.oauth2 import service_account
import ast
import os

load_dotenv()


def get_credentials():
    key = ast.literal_eval(os.environ["BIGQUERY_KEY"])
    credentials = service_account.Credentials.from_service_account_info(key)

    credentials = credentials.with_scopes(
        ['https://www.googleapis.com/auth/cloud-platform'])

    return credentials