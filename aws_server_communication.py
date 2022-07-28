import boto3
import pandas as pd

# Creating the low level functional client
client = boto3.client(
    's3',
    aws_access_key_id = 'AKIASJIEFZIWUUY5K5DG',
    aws_secret_access_key = '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',
    region_name = 'us-east-1'
)
    
# Creating the high level object oriented interface
resource = boto3.resource(
    's3',
    aws_access_key_id = 'AKIASJIEFZIWUUY5K5DG',
    aws_secret_access_key = '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',
    region_name = 'us-east-1'
)

# Fetch the list of existing buckets
clientResponse = client.list_buckets()
    
# Print the bucket names one by one
print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')

# Creating a bucket in AWS S3
location = {'LocationConstraint': 'us-east-1'}
client.create_bucket(
    Bucket='sql.server.shack.demo.4'
)

# Create the S3 object
obj = client.get_object(
    Bucket = 'sql.server.shack.demo.1',
    Key = 'RAJK_ZORK_edges.csv'
)
    
# Read data from the S3 object
data = pd.read_csv(obj['Body'])
    
# Print the data frame
print('Printing the data frame...')
print(data)