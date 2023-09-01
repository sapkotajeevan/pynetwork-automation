import myparamiko

ssh_client = myparamiko.connect('10.10.10.1',22,'jeevan','cisco')
connection = myparamiko.get_shell(ssh_client)
myparamiko.send_command(connection,'enable')
myparamiko.send_command(connection,'cisco')
myparamiko.send_command(connection,'terminal length 0')
output = myparamiko.send_command(connection,'show run')
print(output.decode())
myparamiko.close(ssh_client)
