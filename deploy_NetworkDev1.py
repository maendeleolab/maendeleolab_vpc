#!/usr/bin/python3

from maendeleolab_lib import *

# create VPC
CIDRs_list=[
		'10.7.0.0/20',#us-east-1
		'10.107.0.0/20',#us-east-2
		]

Regions_list=[
		'us-east-1',
		'us-east-2',
		]

for cidr, region in zip(CIDRs_list, Regions_list):
	make_vpc(
		Cidr=cidr, #CIDRs_list 
		Vpc_name='NetworkDev1', #VPC name
		Tag_key='Description', #Tag Key
		Tag_value='Maendeleolab VPC', #Tag Value
		Region=region_id(region) #Regions_list
	)

# -------------------- End ------------------------

