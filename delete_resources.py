#!/usr/bin/env python3

from maendeleolab_lib import *

maendeleolab_infra=[
					'us-east-1', #us-east-1
					'us-east-2', #us-east-2
				   ]

for region in maendeleolab_infra:
	erase_vpcs(region)

# ------------------ End --------------------
