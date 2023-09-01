from netmiko import Netmiko
#from netmiko import ConnectHandler

connection = Netmiko(host='10.10.10.1',username='jeevan',password='cisco',device_type='cisco_ios')

#cisco_device = {'device_type':'cisco_ios',
#                'ip':'10.10.10.1',
#                'username':'jeevan',
#                'password':'cisco',
#                'secret':'cisco',
#                'verbose':True
#                }

#connection = ConnectHandler(**cisco_device)
output = connection.send_command('show ip int br')
print(output)

connection.disconnect()
