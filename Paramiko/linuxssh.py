#I haven't entered password, so don't forget to enter linux password replacing EnterPasswordHere and delete once done.

import paramiko

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('192.168.1.22',port=22,username='jeevan',password='EnterPasswordHere',look_for_keys=False,allow_agent=False)

stdin,stdout,stderr = ssh_client.exec_command('sudo apt update')
stdin.write('EnterPasswordHere\n')

output = stdout.read().decode()
print(output)

ssh_client.close()

with open('log.txt','w') as f:
    f.write(output)
