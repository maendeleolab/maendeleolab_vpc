# maendeleolab_vpc

```
├── build_vpc.py
├── delete_resources.py
├── deploy_NetworkDev1.py
├── maendeleolab_lib.py
└── vpc.log
```

**Context:**

This script was built with the intention to simplify its use. 

It can run on any Linux environment in AWS or on-premises, that is able to install Python 3.6.9 (or higher) and awscli version 2.

It is capable to create a unique VPC, including a primary CIDR and the option to add a secondary CIDR.

The scripts are idempotent. This means, if the resource tag name already exists, it will not create another one.

**Prerequisites:**

It helps to be familiar with Linux basics commands.

Must have awscli version 2 and Python 3.6.9 (or higher) installed.

I recommend dedicating an instance (or on-premises server) to programmatically run the scripts.  

awscli --profile option is not used for simplicity. Assign a role with programmatic access to the instance/server default profile.


**Walk-through:**

**1**  - Make sure to comply with the prerequisites mentions above.

**2**  - Update and install the latest packages of your Linux distribution system.

**3**  - Clone this repo to the instance/server using the syntax below.

```
git clone git@github.com:maendeleolab/maendeleolab_vpc.git
```

**4**  - cd to folder maendeleolab_vpc

```
cd maendeleolab_vpc
```

**5**  - List the files in the folder with the ls command. It should match the files below.
```	
Note: A file named vpc.log will be created to store the scripts logs, when you run the script for the first time.
Remember to use it to monitor your environment or troubleshoot an issue.
```

```
README.md
build_vpc.py
delete_resources.py
deploy_NetworkDev1.py
maendeleolab_lib.py
```

**6**  - I recommend running the script **NetworkDev1.py** to see what the expected results look like. 

	   It will create a VPC named NetworkDev1 in us-east-1 and us-east-2 with their respective CIDR ranges.

	   This script will become your building block for additional VPC scripts. 

	   You have the option to copy the script to another file name and edit it.

```
./NetworkDev1.py or python3 NetworkDev1.py
```

**7**  - Verify the expected results are present in the VPC console. 

**8**  - Run the script again to verify idempotency is working as expected. 

**9**  - VPC resources do not cost you anything, but in case you decide to delete the VPCs. You can run the script **delete_resources.py**
	
	**Note:**The script all delete all VPC resources that do not have any dependencies. 
	
	This means, if subnets and route tables are not associated to the VPC, the VPC will be deleted. 

```
./delete_resources.py or python3 delete_resources.py
```

**10** - If you get to this step, congratulations! for being brave to take action on using this repo. 

	
