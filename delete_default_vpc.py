import boto3

client = boto3.client('ec2')
response = client.describe_regions()

regions = []
for i in  response['Regions']:
    regions.append(i['RegionName'])

for region in regions:

    print('Deleting default vpc for ' + region)

    client = boto3.client('ec2',region_name=region)


    def describe_all_vpcs(client):
        response = client.describe_vpcs(

        )

        # print(response)

        for i in response['Vpcs']:
            if i['IsDefault'] == True:
                return i['VpcId']


    def get_internet_gateway(client, default_vpc_id):
        response = client.describe_internet_gateways(
            Filters=[
                {
                    'Name': 'attachment.vpc-id',
                    'Values': [
                        default_vpc_id,
                    ]
                },
            ],

        )
        # print(response)

        for igw in response['InternetGateways']:
            return igw['InternetGatewayId']


    def detach_internet_gateway(client, igw_id, vpc_id):
        try:
            response = client.detach_internet_gateway(
                InternetGatewayId=igw_id,
                VpcId=vpc_id
            )
            print('Internet gateway detached successfully')
        except Exception as e:
            print(e)


    def delete_internet_gateway(client, igw_id):
        try:
            response = client.delete_internet_gateway(
                InternetGatewayId=igw_id
            )
            print('Successfully Deleted Internet Gateway')
        except Exception as e:
            print(e)


    def describe_and_delete_subnets(client, vpc_id):
        response = client.describe_subnets(
            Filters=[
                {
                    'Name': 'vpc-id',
                    'Values': [
                        vpc_id,
                    ]
                },
            ],

        )
        for subnet in response['Subnets']:
            client.delete_subnet(
                SubnetId=subnet['SubnetId']
            )
        print('successfully deleted subnets')


    def delete_default_vpc(client, vpc_id):
        response = client.delete_vpc(
            VpcId=vpc_id,
        )
        print('Successfully deleted vpc', vpc_id)


    default_vpc_id = describe_all_vpcs(client)

    default_igw_id = get_internet_gateway(client, default_vpc_id)

    detach_internet_gateway(client, default_igw_id, default_vpc_id)

    delete_internet_gateway(client, default_igw_id)

    describe_and_delete_subnets(client, default_vpc_id)

    delete_default_vpc(client, default_vpc_id)



