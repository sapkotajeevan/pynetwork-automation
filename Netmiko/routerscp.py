## Username : admin  IP: 10.10.10.40   Router Disk : disk0:

from netmiko import ConnectHandler
from netmiko import file_transfer

cisco_device = {
                'device_type':'cisco_ios',
                'ip':'10.10.10.40',
                'port':22,
                'username':'admin',
                'secret':'cisco',
                'password':'cisco',
                'verbose':True
                }

connection = ConnectHandler(**cisco_device)

output = file_transfer(connection,source_file='devices.txt',dest_file='devices.txt',file_system='disk0:',direction='put',overwrite_file=True)
print(output)

connection.disconnect()
