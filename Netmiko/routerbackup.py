## To backup running config of each routers in the format Hostname-Year-Month-Day (Router1-2020-07-22.txt)
# 1. Read the content of devices.txt as list
# 2. Iterate through list that contains ip addresses
# 3. Establish SSH through ConnectHandler function
# 4. Enable and send command 'show run'
# 5. Make a variable that stores filename as required
# 6. Write the output of 'show run' into that filename

import datetime
from netmiko import ConnectHandler

with open('devices.txt') as f:
    devices = f.read().splitlines()

for ip in devices:
    cisco_device = {
                    'device_type':'cisco_ios',
                    'ip':ip,
                    'port':22,
                    'username':'jeevan',
                    'secret':'cisco',
                    'password':'cisco',
                    'verbose':True
                    }

    connection = ConnectHandler(**cisco_device)

    print('Connected to device : ' + ip)
    print('Entering enable mode...')
    connection.enable()

    output = connection.send_command('show run')
    print(output)

    prompt = connection.find_prompt()
    hostname = prompt[:-1]

    date = datetime.datetime.now()
    today = str(date.year) + '-' + str(date.month) + '-' + str(date.day)

    file = hostname + '-' + today

    with open(file +'.txt','w') as backup:
        print('Saving configuration of device : ' + ip)
        backup.write(output)
        print('Backup file : ' + file + '.txt created')
        print('#' * 30)

    connection.disconnect()
