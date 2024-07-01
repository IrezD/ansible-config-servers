import boto3

ec2 = boto3.client("ec2")

COUNT = 1

def create_server():
    ec2.run_instances(
        ImageId='ami-01e444924a2233b07',
        InstanceType='t2.micro',
        MaxCount=COUNT,
        MinCount=COUNT,
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
    
create_server()