import paramiko
import getpass
from scp import SCPClient

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.1.22',port=22,username='jeevan',password='Rj@me123',look_for_keys=False,allow_agent=False)

scp = SCPClient(ssh_client.get_transport())

# To copy files and folder from local to remote location
scp.put('log.txt','logreceived.txt')
scp.put('Directory',recursive=True,remote_path='/home/jeevan/Desktop')

# To fetch files from remote to local location
scp.get('/etc/passwd','passwd')

scp.close()
