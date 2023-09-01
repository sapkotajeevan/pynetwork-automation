#  Task : To ask user for the interface name and 'no shut' the interface if it's down
#  HouseKeeping stuffs for SSH Connection using ConnectHandler
#  Store the result of 'show int brief'
#  Make a dict() object with Interfaces(key) and Port Staus(value)
#  Ask user for interface name
#  If interface is down run 'no sh' command else print logical output
#  Close ssh

from netmiko import ConnectHandler
import csv

cisco_device = {
                    'device_type':'cisco_ios',
                    'ip':'10.10.10.1',
                    'username':'jeevan',
                    'password':'cisco',
                    'secret':'cisco',
                    'port':22,
                    'verbose':True

}

connection = ConnectHandler(**cisco_device)

connection.enable()

output = connection.send_command('show ip interface brief')
print(output)

with open('int_details.txt','w') as f:
    f.write(output)
    
with open('int_details.txt') as f:
    int_list = f.read().splitlines()
    

int_list = int_list[1:]
new_list = list()

for item in int_list:
    tmp = item.split(' ')
    new_list.append(tmp)
print(new_list)


connection.disconnect()