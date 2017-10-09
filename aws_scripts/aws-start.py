import boto3
import sys


def get_instance_info(ec2_client):
    response = ec2_client.describe_instances()
    instances = [x for r in response['Reservations'] for x in r['Instances']]
    keys = ['InstanceId', 'InstanceType', 'State', 'PublicDnsName']
    return {instance['Tags'][0]['Value']: {k: instance[k] for k in keys}
            for instance in instances}


def start_instance(ec2_client, name):
    from time import sleep
    instance_info = get_instance_info(ec2_client)
    response = ec2_client.start_instances(
        InstanceIds=[instance_info[name]['InstanceId']])
    si = response['StartingInstances']
    states = ['running', 'pending']
    if len(si) != 1 or si[0]['CurrentState']['Name'] not in states:
        print("Something went wrong!", response)
        return ""
    else:
        while True:
            sleep(0.5)
            dns_name = get_instance_info(ec2_client)[name]['PublicDnsName']
            if dns_name:
                return dns_name


def main():
    instance_name = sys.argv[1]
    region_name = sys.argv[2] if len(sys.argv) > 2 else 'us-west-2'
    ec2 = boto3.client('ec2', region_name=region_name)
    print(start_instance(ec2, instance_name))


if __name__ == '__main__':
    main()
