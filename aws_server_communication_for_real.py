import boto3
import pandas as pd

client = boto3.client(
    's3',
    aws_access_key_id = 'AKIASJIEFZIWUUY5K5DG',
    aws_secret_access_key = '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',
    region_name = 'us-east-1'
)

#location = {'LocationConstraint': 'us-east-1'}
#client.create_bucket(
#    Bucket='szovegek'
#)
    
clientResponse = client.list_buckets()
print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')


client.upload_file(
    Filename="C:/rajk_zork_dork_biztonsagi_mentesek/RAJK_ZORK_edges.csv",
    Bucket="szovegek",
    Key="RAJK_ZORK_edges.csv",
)


client.upload_file(
    Filename="C:/rajk_zork_dork_biztonsagi_mentesek/RAJK_ZORK_nodes.csv",
    Bucket="szovegek",
    Key="RAJK_ZORK_nodes.csv",
)


# Create the S3 object
RAJK_ZORK_edges_from_AWS_server = client.get_object(
    Bucket = 'szovegek',
    Key = 'RAJK_ZORK_edges.csv'
)
    
# Create the S3 object
RAJK_ZORK_nodes_from_AWS_server = client.get_object(
    Bucket = 'szovegek',
    Key = 'RAJK_ZORK_nodes.csv'
)
    
# Read data from the S3 object
RAJK_ZORK_edges_data = pd.read_csv(RAJK_ZORK_edges_from_AWS_server['Body'])

# Read data from the S3 object
RAJK_ZORK_nodes_data = pd.read_csv(RAJK_ZORK_nodes_from_AWS_server['Body'])

print('Printing the data frame...')
print(RAJK_ZORK_edges_data)

response = client.put_object(
    Body=user_ids,
    Bucket='string',
    Key='string',
)


import boto3

some_binary_data = b'Here we have some data'
more_binary_data = b'Here we have some more data'

# Method 1: Object.put()
s3 = boto3.resource('s3')
object = s3.Object('my_bucket_name', 'my/key/including/filename.txt')
object.put(Body=some_binary_data)

# Method 2: Client.put_object()
client = boto3.client('s3')
client.put_object(Body=more_binary_data, Bucket='my_bucket_name', Key='my/key/including/anotherfilename.txt')