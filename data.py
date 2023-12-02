
# Define a query (modify according to your needs)
from google.cloud import bigquery

def fetch_data():
    client = bigquery.Client(project='161603559480')
    query = """
    SELECT * FROM `bigquery-public-data.chicago_crime.crime`
    WHERE year = 2017
    LIMIT 1000
    """
    query_job = client.query(query)
    results = query_job.to_dataframe()
    return results

