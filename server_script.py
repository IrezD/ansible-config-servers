import boto3, os
from dotenv import load_dotenv

load_dotenv()

ec2 = boto3.client("ec2")

SECURITY_GROUP_ID = os.getenv("SECURITY_GROUP_ID")
INSTANCE_TYPE = os.getenv("INSTANCE_TYPE")
KEYNAME = os.getenv("KEYNAME")

COUNT = 2

# ** Create Ansible Server (Ubuntu)

def create_server():
    server = ec2.run_instances(
        ImageId='ami-01e444924a2233b07',
        InstanceType=INSTANCE_TYPE,
        MaxCount=COUNT,
        MinCount=COUNT,
        KeyName=KEYNAME,
        SecurityGroupIds=[SECURITY_GROUP_ID],
        TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Ansible_server'
                },
            ]
        },
     ],
    )
    
    print (server)
    
    
# ** Describes The Server

def describe_server():
    response = ec2.describe_instances(
        MaxResults=6
    )

    METADATA = response['Reservations'][0]['Instances'][0]

    INSTANCE_STATE = METADATA['State']['Name']
    PUBLIC_IP = METADATA['PublicIpAddress'] 
       
    print(f"{response} \n ****************************************************")
    print(f"Instance is {INSTANCE_STATE}. \nPublic IP: {PUBLIC_IP} ")


# ** Start Server

def start_server():
    print("Which Instance do you wish Start? \n")
    ec2.start_instances(
        InstanceIds = input("Enter the instance-id: ").split()
    )
    

    print(f"Server is Running.")

    # print(f"Server - {INSTANCE_ID} is now Running.")

# ** Stop Server

def stop_server():
    print("Which Instance do you wish Stop? \n")
    ec2.stop_instances(
        InstanceIds = input("Enter the instance-id: ").split()

    )

    print(f"Server has been Stopped.")


# ** Call Any Function to Run

describe_server()
