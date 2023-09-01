from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret':'cisco'}
ios = driver('192.168.122.9','jeevan','cisco',optional_args = optional_args)

ios.open()

output = ios.ping('192.168.122.190')

# for item in output:
#     print(item)

dump = json.dumps(output,sort_keys=True,indent=4)
print(dump)

ios.close()