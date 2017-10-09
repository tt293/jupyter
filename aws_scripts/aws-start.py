import boto3
import sys
import aws_common


def main():
    instance_name = sys.argv[1]
    region_name = sys.argv[2] if len(sys.argv) > 2 else 'us-west-2'
    ec2 = boto3.client('ec2', region_name=region_name)
    print(aws_common.start_instance(ec2, instance_name))


if __name__ == '__main__':
    main()
