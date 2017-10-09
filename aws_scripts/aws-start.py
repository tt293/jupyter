import boto3
import sys
import aws_common


def get_instance_info(ec2_client):
    response = ec2_client.describe_instances()
    instances = [x for r in response['Reservations'] for x in r['Instances']]
    keys = ['InstanceId', 'InstanceType', 'State', 'PublicDnsName']
    return {instance['Tags'][0]['Value']: {k: instance[k] for k in keys}
            for instance in instances}


def main():
    instance_name = sys.argv[1]
    region_name = sys.argv[2] if len(sys.argv) > 2 else 'us-west-2'
    ec2 = boto3.client('ec2', region_name=region_name)
    print(aws_common.start_instance(ec2, instance_name))


if __name__ == '__main__':
    main()
