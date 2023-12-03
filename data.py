from google.cloud import bigquery

def fetch_data():
    client = bigquery.Client(project='161603559480')
    query = """
    SELECT case_number, date, primary_type, description, location_description, arrest, domestic, CAST(district AS INT64) AS district, year
    FROM `bigquery-public-data.chicago_crime.crime`
    WHERE year BETWEEN 2015 AND 2023
    LIMIT 10000
    """
    query_job = client.query(query)
    results = query_job.to_dataframe()
    return results
