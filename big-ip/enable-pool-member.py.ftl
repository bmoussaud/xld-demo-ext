#!/usr/bin/python

import sys
from sys import argv

bigip_address = '${container.address}'
bigip_user = '${container.username}'
bigip_pass = '${container.password}'
active_partition = '${container.partition}'
poolmember_pool = '${poolmember.bigIpPool}'
poolmember_address = '${poolmember.bigIpAddress}'
poolmember_port = '${poolmember.bigIpPort}'

print 'Connecting to BIG-IP at [' + bigip_address + '] as user [' + bigip_user + ']'
print 'Setting active partition to [' + active_partition + ']'
print 'Enabling pool member [' + poolmember_address + ':' + poolmember_port + '] in pool [' + poolmember_pool + ']'
print 'Done'
