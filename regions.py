import boto3

client = boto3.client('ec2')
response = client.describe_regions()

print(response)

regions = []
for i in  response['Regions']:
    regions.append(i['RegionName'])


print(regions)