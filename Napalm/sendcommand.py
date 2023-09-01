from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret':'cisco'}
ios = driver('10.10.10.40','admin','cisco',optional_args = optional_args)

ios.open()

commands = ['show version','show run']
output = ios.cli(commands)

# dump = json.dumps(output)
# print(dump)


for k,v in output.items():
    print(k+v)

ios.close()