#!/usr/bin/python3

Goal = '''
to create a vpc in aws
Author: Pat@Maendeleolab
'''

#Module imports
import logging, sys, os, json
from datetime import datetime
from time import sleep

#Path to local home and user folder
FPATH = os.environ.get('ENV_FPATH')

#logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p ',\
									filename=FPATH+'/cloudNetworkSpecialty/vpc/vpc.log', level=logging.INFO)

#adding flexibility for regions
def region_id(name='us-east-1'):
        return name # e.g: 'us-east-1'

def verify_vpc(Vpc_name, region='us-east-1'):
	''' Verifies if VPC exists already '''
	try:
		output = os.popen('aws ec2 describe-vpcs --filters Name=tag:Name,Values=' + Vpc_name + ' --region '+ region).read()
		vpc_data = json.loads(str(output))
		if len(vpc_data['Vpcs']) > 0:
			logging.info(f'{Vpc_name} already exists in {region} ...')
			print(f'{Vpc_name} already exists in {region} ...')
			return 1
	except Exception as err:
		logging.info(err)
		print(f'verify_vpc {Vpc_name} error logged in vpc.log ...')

#create vpc
def make_vpc(**kwargs):
	''' Creates VPC '''
	try:
		print(f'Create VPC {kwargs["Vpc_name"]} in {kwargs["Region"]} ...')
		if verify_vpc(kwargs['Vpc_name'], kwargs['Region']) == 1:
			pass
		else:
			os.system("aws ec2 create-vpc \
				--tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=" + kwargs['Vpc_name'] + "},\
									  {Key=" + kwargs['Tag_key'] + ",Value=" + kwargs['Tag_value'] + "}]'\
				--cidr-block " + kwargs['Cidr'] + "\
				--region " + kwargs['Region'] 
			)
			logging.info('Created VPC:' + kwargs['Vpc_name'])
	except Exception as err:
		logging.info(err)
		print(f'Create VPC {Vpc_name} error logged in vpc.log ...')

def update_vpc(**kwargs):
	''' Adds additional configurations to VPC '''
	try:
		print(f'Additional CIDR: {kwargs["Cidr"]} for VPC {kwargs["Vpc_name"]} in {kwargs["Region"]}...')
		os.system("aws ec2 associate-vpc-cidr-block \
		--cidr-block " + kwargs['Cidr'] + " \
		--vpc-id " + kwargs['Vpc_Id'] + " \
		--region " + kwargs['Region']
		)
		logging.info(f'Additional CIDR: {kwargs["Cidr"]} for VPC {kwargs["Vpc_Id"]}...')
	except Exception as err:
		logging.info(err)
		print(f'Additonal CIDR {kwargs["Cidr"]} error logged in vpc.log ...')

#get vpc id 
def get_VpcId(Vpc_name, region='us-east-1'):
	''' Gets vpc id from json output and can be used in deploy scripts '''
	try:
		output = os.popen('aws ec2 describe-vpcs --filters Name=tag:Name,Values=' + Vpc_name + ' --region '+ region).read()
		vpc_data = json.loads(str(output))
		data = vpc_data['Vpcs'][0]['VpcId']
		return data
	except Exception as err:
		logging.info(err)
		print(f'Logging get_VpcId {Vpc_name} to vpc.log ...') 

def get_AccountId(Vpc_name, region='us-east-1'):
	''' Gets resource id from json output and can be used in deploy scripts '''
	try:
		output = os.popen('aws ec2 describe-vpcs --filters Name=tag:Name,Values=' + Vpc_name + ' --region '+ region).read()
		vpc_data = json.loads(str(output))
		data = vpc_data['Vpcs'][0]['OwnerId']
		return data
	except Exception as err:
		logging.info(err)
		print(f'Logging get_AccountId {Vpc_name} to vpc.log ...') 

def destroy_vpc(Vpc_id, region='us-east-1'):
	''' Destroys VPC '''
	try:
		os.system("aws ec2 delete-vpc --vpc-id " + Vpc_id + " --region " + region)
		logging.info("Deleted VPC Id: " + Vpc_id + " in region: " + region)
	except Exception as err:
		logging.info(err)
		print(f'Logging destroy_vpc {Vpc_id} in vpc.log ...')

def erase_vpcs(region='us-east-1'):
	''' Deletes all vpcs that do not have any dependencies '''
	try:
		output = os.popen('aws ec2 describe-vpcs  --region ' + region).read()
		vpc_data = json.loads(str(output))
		for data in vpc_data['Vpcs']:
			print('Logging: ' + data['VpcId'] + '...')
			destroy_vpc(data['VpcId'], region=region)
			logging.info("Logging erase_vpcs: " + data['VpcId'] + " in region: " + region)

		new_data = json.dumps(data, indent=2)
		print(new_data)
	except Exception as err:
		logging.info(err)
		print('Logging erase_vpcs error to vpc.log ...')


# ------------------------------- End ---------------------------------

