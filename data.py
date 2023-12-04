from google.cloud import bigquery
from google.oauth2 import service_account
import os

def fetch_data():
    # Path to the service account key file
    key_path = os.path.join(os.path.dirname(__file__), 'cop3530-final-cece71eb5bc6.json')

    # Load credentials from the key file
    credentials = service_account.Credentials.from_service_account_file(key_path)

    # Initialize the BigQuery Client with the credentials
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)

    query = """
    SELECT case_number, date, primary_type, description, location_description, arrest, domestic, CAST(district AS INT64) AS district, year
    FROM `bigquery-public-data.chicago_crime.crime`
    WHERE year BETWEEN 2015 AND 2023
    LIMIT 100000
    """

    query_job = client.query(query)
    results = query_job.to_dataframe()
    return results
