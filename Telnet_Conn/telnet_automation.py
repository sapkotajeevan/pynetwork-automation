import telnetlib
import getpass
import time

my_devices = ['10.10.10.1','10.10.10.2','10.10.10.3']

for devices in my_devices:
    tn = telnetlib.Telnet(devices)
    username = 'jeevan'
    password = getpass.getpass()

    tn.read_until(b'Username: ')
    tn.write(user.encode() + b'\n')

    tn.read_until(b'Password: ')
    tn.write(password.encode() + b'\n')

    tn.write(b'enable\n')
    tn.write(password.encode() + b'\n')
    tn.write(b'config t\n')
    tn.write(b'no ip route *\n')
    tn.write(b'ip route 0.0.0.0 0.0.0.0 10.10.10.10\n')
    tn.write(b'end\n')
    tn.write(b'show ip route\n')
    tn.write(b'exit\n')

    result = tn.read_all().decode()
    print(result)
    print('#############################################')
    time.sleep(1)
