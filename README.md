# maendeleolab_vpc
![GitHub commit activity](https://img.shields.io/github/last-commit/maendeleolab/maendeleolab_vpc)

<img src="/images/banner.png" width=400>

```
├── build_vpc.py
├── delete_resources.py
├── deploy_NetworkDev1.py
├── maendeleolab_lib.py
└── vpc.log
```

## [Context](#Context)

- This repo was built to create a basic VPC construct to use with IPv4. 

- It can be used on any Linux environment in AWS or on-premises. 

- Install Python 3.6.9 (or higher) and awscli version 2.

- It creates a unique VPC, including a primary CIDR and the option to add a secondary CIDR. 

- The scripts are idempotent. 

- The line above means, if the resource is tagged with a name that already exists, it will not create another one.

## [Prerequisites](#Prerequisites)

- Please watch the [requirements steps](https://www.youtube.com/watch?v=gMM-d1uZ0Ks&t=12s) 

- It helps to be familiar with Linux basics commands.

- Must have awscli version 2 and Python 3.6.9 (or higher) installed.

- I recommend dedicating an instance (or on-premises server) to programmatically run the scripts.  

- Assign a role with programmatic access to the instance/server default profile.

- Run this command 'export ENV_FPATH="folder-path" ' 

- Replace folder-path with your folder location (this the folder, where you will download the repo). 

See the example below.

```
export ENV_FPATH="/home/ubuntu"
```

## [Walk-through](#Walk-through)


Watch [tutorial](https://youtu.be/SCcGe9pr5Z0) on youtube for step by step instructions.

**1**  - Make sure to comply with the prerequisites mentioned above.

**2**  - Update and install the latest packages of your Linux distribution system.

**3**  - Clone this repo to the instance/server using the syntax below.

```
git clone https://github.com/maendeleolab/maendeleolab_vpc.git
```

**4**  - cd to folder maendeleolab_vpc

```
cd maendeleolab_vpc
```

**5**  - List the files in the folder with the **ls** command. It should match the files below.

**Note:** A file named **vpc.log** will be created to store the scripts logs, when you run the script for the first time.

Remember to use it to monitor your environment or troubleshoot an issue.


```
README.md
LICENSE
images
build_vpc.py
delete_resources.py
deploy_NetworkDev1.py
maendeleolab_lib.py
```

**6**  - I recommend running the script **NetworkDev1.py** to see what the expected results look like. 

It will create a VPC named NetworkDev1 in us-east-1 and us-east-2 with their respective CIDR ranges.

This script will become your building block for additional VPC scripts and your single source of truth. 

You have the option to copy the script to another file name and edit it.

```
./NetworkDev1.py or python3 NetworkDev1.py
```

**7**  - Verify the expected results are present in the VPC console. 

**8**  - Run the script again to verify idempotency is working as expected. 

**9**  - VPC resources do not cost you anything, but in case you decide to delete the VPCs. You can run the script **delete_resources.py**
	
**Note:** The script deletes all VPC resources that do not have any dependencies. 
	
This means, if subnets and route tables are not associated to the VPC, the VPC will be deleted. 

```
./delete_resources.py or python3 delete_resources.py
```

**11** - If you get to this step, congratulations for being brave to do it! 

## [Support](#Support)
If you find this script useful, please support it with a shout out on your favorite social media platform!

![Twitter](https://img.shields.io/twitter/follow/maendeleolab?style=social)
```
Twitter : @maendeleolab
Instagram : @maendeleolab
TitTok : @pat_maendeleolab
```
## [License](#License)
GNU GENERAL PUBLIC LICENSE

	
