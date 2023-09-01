class Device:
    def __init__(self,ip,username,password,connection=None):
        self.ip = ip
        self.username = username
        self.password = password
        self.connection = connection

    def connect(self):
        import telnetlib
        self.connection = telnetlib.Telnet(self.ip)

    def authenticate(self):
        self.connection.read_until(b'Username: ')
        self.connection.write(self.username.encode() + b'\n')
        self.connection.read_until(b'Password: ')
        self.connection.write(self.password.encode() + b'\n')

    def execute(self,command):
        self.connection.write(command.encode() + b'\n')

    def show(self):
        output = self.connection.read_all().decode('utf-8')
        return output

with open('devices.txt','r') as f:
    device = f.read().splitlines()     ## Reading ip and loopback addresses in list

ip = list()  ## Creating new list so as to separate ip and looback addresses

for item in device:
    tmp = item.split(':')  ## Split (10.10.10.1:1.1.1.1) as [10.10.10.1 , 1.1.1.1.]
    ip.append(tuple(tmp))  ## Making tuple as [(10.10.10.1 , 1.1.1.1) , (10.10.10.2) , (2.2.2.2) and so on]

for element in ip:
    router = Device(element[0],'jeevan','cisco')
    router.connect()
    router.authenticate()
    router.execute('enable')
    router.execute('cisco')  ## This is enable Password
    router.execute('terminal length 0')
    router.execute('config t')
    router.execute('int loopback 0')
    router.execute('ip address ' + str(element[1]) + ' 255.255.255.255')
    router.execute('exit')
    router.execute('router ospf 1')
    router.execute('network 0.0.0.0 0.0.0.0 area 0')
    router.execute('end')
    router.execute('show ip protocols')
    router.execute('exit')

    output = router.show()
    print(output)
    print('################################################################')
