#!/usr/bin/python3

from maendeleolab_lib import *

# Each VPC CIDR in CIDRs_list is assigned to a region in Regions_list
CIDRs_list=[
		'10.7.0.0/20',# CIDR for us-east-1
		'10.107.0.0/20',# CIDR for us-west-2
		]

Secondary_CIDRs_list=[
		'10.0.1.0/24', # Additional CIDR block for us-east-1
		'10.0.2.0/24', # Additional CIDR block for us-west-2
		]

Regions_list=[
		'us-east-1', # 10.7.0.0/20 is assigned to us-east-1 VPC
		'us-west-2', # 10.107.0.0/20 is assigned to us-west-2 VPC
		]

# Create VPC NetworkDev1 in each region defined in the lists above
for cidr, region in zip(CIDRs_list, Regions_list):
	make_vpc(
		Cidr=cidr, # CIDRs_list 
		Vpc_name='NetworkDev1', # VPC name
		Tag_key='Description', # Tag Key
		Tag_value='Maendeleolab VPC', # Tag Value
		Region=region_id(region) # Regions_list
	)

# Add a secondary CIDR to VPC
for cidr, region in zip(Secondary_CIDRs_list, Regions_list):
	update_vpc(
			Cidr=cidr, # Additional CIDR list
			Vpc_name='NetworkDev1', # VPC name
			Vpc_Id=get_VpcId('NetworkDev1',region), # Get VPC Id
			Region=region
	)

# ----------------------- End ------------------------

