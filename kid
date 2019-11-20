import boto3

def get_kid(region_name):
    client = boto3.client('kms', region_name=region_name)
    response = client.list_aliases()

    req_alias = 'alias/aws/ebs'

    kid = None

    for alias in response['Aliases']:
        alias_name = alias['AliasName']
        if alias_name == req_alias:
            kid = alias['TargetKeyId']

    return kid

kid = get_kid('us-east-1')

print (kid)
