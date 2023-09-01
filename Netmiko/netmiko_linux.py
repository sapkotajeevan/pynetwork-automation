from netmiko import ConnectHandler

linux = {
            'device_type':'linux',
            'ip':'192.168.1.22',
            'username':'jeevan',
            'password':'Rj@me123',
            'secret':'Rj@me123',   # Sudo password
            'port':22,
            'verbose':True
        }

connection = ConnectHandler(**linux)

connection.enable()  # hitting sudo su command

output = connection.send_command('apt-get update && apt-get -y install apache2')   #Put your command here
print(output)

connection.disconnect()
