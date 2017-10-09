import boto3
import sys


def get_instance_info(ec2_client):
    response = ec2_client.describe_instances()
    instances = [x for r in response['Reservations'] for x in r['Instances']]
    keys = ['InstanceId', 'InstanceType', 'State', 'PublicDnsName']
    return {instance['Tags'][0]['Value']: {k: instance[k] for k in keys}
            for instance in instances}


def stop_instance(ec2_client, name):
    instance_info = get_instance_info(ec2_client)
    response = ec2_client.stop_instances(
        InstanceIds=[instance_info[name]['InstanceId']])
    si = response['StoppingInstances']
    states = ['stopping', 'stopped']
    if len(si) != 1 or si[0]['CurrentState']['Name'] not in states:
        sys.stderr.write("Something went wrong!", response)
        return False
    else:
        return True


def main():
    instance_name = sys.argv[1]
    region_name = sys.argv[2] if len(sys.argv) > 2 else 'us-west-2'
    ec2 = boto3.client('ec2', region_name=region_name)
    print(stop_instance(ec2, instance_name))


if __name__ == '__main__':
    main()
