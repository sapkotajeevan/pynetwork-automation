import telnetlib
import getpass

host = '10.10.10.1'
user = 'jeevan'
password = getpass.getpass()

tn =telnetlib.Telnet(host)
tn.read_until(b'Username: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'Password: ')
tn.write(password.encode() + b'\n')

tn.write(b'enable\n')
tn.write(b'cisco\n')
tn.write(b'terminal length 0\n')
tn.write(b'config t\n')
tn.write(b'int loopback 0\n')
tn.write(b'ip address 1.1.1.1 255.255.255.255\n')
tn.write(b'exit\n')
tn.write(b'exit\n')
tn.write(b'exit\n')

result = tn.read_all().decode()
print(result)
