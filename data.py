from google.cloud import bigquery

# Create a BigQuery client using your project ID
client = bigquery.Client(project='161603559480')

# Define a query (modify according to your needs)
query = """
SELECT * FROM `bigquery-public-data.chicago_crime.crime`
LIMIT 100
"""

# Run the query
query_job = client.query(query)

# Convert the results to a pandas DataFrame
results = query_job.to_dataframe()

# Display the first few rows of the DataFrame
print(results.head())
