def lambda_handler(event,context):
    import boto3

    client = boto3.client('kms')

    response = client.list_aliases()
    i = 0

    for Aliases in response:

        print ('value of i : ', i)
        desired_alias = response['Aliases'][i]['AliasName']
        if desired_alias == 'alias/aws/ebs':
                kid = response['Aliases'][i]['TargetKeyId']
                print ('value of i at desired_alias : ', i)
                print (desired_alias)
                print (kid)

        i = i+1

#print (response)
