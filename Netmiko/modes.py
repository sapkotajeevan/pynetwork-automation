from netmiko import ConnectHandler

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

connection.enable()   ## Go to enable mode

commands = ['no int loopback 0','int loopback 0','ip address 1.1.1.1 255.255.255.0','exit','do show run']

output = connection.send_config_set(commands)   ## Automatically goes to config mode and executes all the commands
print(output)

output = connection.send_command_expect('write memory')  ## Same as send_command but used with command that take more time to execute
print(output)

connection.disconnect()
