
import boto3



def check_user_existence(client,user_name):
    try:
        users = []
        response = client.list_users(MaxItems=999)
        for i in response['Users']:
            users.append(i['UserName'])
        if user_name in  users :
            print('User exists. Going for deletion')
            delete_user_finally(client,user_name)
        else:
            print('User  ' + user_name + ' does not exist. Nothing to do here')

    except Exception as e:
        print(e)



def delete_login_profile(client, user_name):
    try:
        response = client.get_login_profile(UserName=user_name)
        if response != {}:
            client.delete_login_profile(UserName=user_name)
            print("User Login Profile Deleted")
    except Exception as e:
        print("No User login profile found ")

def delete_access_keys(client, user_name) :
    try:
        response = client.list_access_keys(UserName=user_name)
        if response['AccessKeyMetadata'] != []:
            for i in response['AccessKeyMetadata']:
                client.delete_access_key(
                    UserName=user_name,
                    AccessKeyId=i['AccessKeyId']
                )
            print("User Access Keys Deleted")
    except Exception as e:
        print(e)
def delete_signing_certificates(client,user_name):
    try:
        response = client.list_signing_certificates(UserName=user_name)
        if response['Certificates'] != []:
            for i in response['Certificates']:
                client.delete_signing_certificate(
                    UserName=user_name,
                    CertificateId=i['CertificateId']
                )
            print("User Signing Certificates Deleted")
    except Exception as e:
        print(e)


def delete_ssh_public_keys(client,user_name):
    try:
        response = client.list_ssh_public_keys( UserName=user_name)
        if response['SSHPublicKeys'] != []:
            for i in response['SSHPublicKeys']:
                client.delete_ssh_public_key(
                    UserName=user_name,
                    SSHPublicKeyId=i['SSHPublicKeyId']
                )
            print('SSH User Keys Deleted')


    except Exception as e:
        print(e)

def delete_git_credentials(client,user_name):
    try:
        response = client.list_service_specific_credentials(
            UserName=user_name,
            ServiceName='codecommit.amazonaws.com'
        )
        if response['ServiceSpecificCredentials'] != []:
            for i in response['ServiceSpecificCredentials']:
                client.delete_service_specific_credential(
                    UserName=user_name,
                    ServiceSpecificCredentialId=i['ServiceSpecificCredentialId']
                )
            print('Git Credentials deleted')
    except Exception as e:
        print(e)

def delete_mfa(client,user_name):
    try:
        response = client.list_mfa_devices(UserName=user_name)
        if response['MFADevices'] != []:
            for i in response['MFADevices']:
                client.deactivate_mfa_device(
                    UserName=user_name,
                    SerialNumber=i['SerialNumber']
                )
                print('Deactivated MFA')
                client.delete_virtual_mfa_device(
                    SerialNumber=i['SerialNumber']
                )
            print('Deleted MFA device')
    except Exception as e:
        print(e)


def delete_inline_user_policies(client,user_name):
    try:
        response = client.list_user_policies(UserName=user_name)
        if response['PolicyNames'] != []:
            for i in response['PolicyNames']:
                client.delete_user_policy(
                    UserName=user_name,
                    PolicyName=i
                )
            print('inline policies deleted')
    except Exception as e:
        print(e)


def detach_attached_policies(client,user_name):
    try:
        response = client.list_attached_user_policies(UserName=user_name)
        if response['AttachedPolicies'] != []:
            for i in response['AttachedPolicies']:
                print(i['PolicyArn'])
                response = client.detach_user_policy(
                    UserName=user_name,
                    PolicyArn=i['PolicyArn']
                )
            print ('Detached policies')
    except Exception as e:
        print(e)


def remove_user_from_groups(client,user_name):
    try:
        response = client.list_groups_for_user(UserName=user_name)
        for i in response['Groups']:
            client.remove_user_from_group(
                GroupName=i['GroupName'],
                UserName=user_name
            )
        print('removed user from groups')


    except Exception as e:
        print(e)
def delete_iam_user(client,user_name):
    try:
        response = client.delete_user(UserName=user_name)

        print('Deleted ' + user_name + ' Successfully')

    except Exception as e:
        print(e)

def delete_user_finally(client,user_name):
    delete_login_profile(client, user_name)
    delete_access_keys(client, user_name)
    delete_signing_certificates(client, user_name)
    delete_ssh_public_keys(client, user_name)
    delete_git_credentials(client, user_name)
    delete_mfa(client, user_name)
    delete_inline_user_policies(client, user_name)
    detach_attached_policies(client, user_name)
    remove_user_from_groups(client, user_name)
    delete_iam_user(client, user_name)



client = boto3.client('iam')
user_name = 'test_user1@rivigo.com'

check_user_existence(client, user_name)
