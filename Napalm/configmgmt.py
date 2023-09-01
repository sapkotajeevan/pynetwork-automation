from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret':'cisco'}
ios = driver('10.10.10.40','admin','cisco',optional_args = optional_args)

ios.open()

ios.load_replace_candidate(filename='config.txt')
diff = ios.compare_config()
if len(diff):
    print(diff)
    print('Commit changes...')
    ios.commit_config()
    print('Done')
else:
    # print('No changes required...')
    # ios.discard_config()
    print('Rolling Back Configuration...')
    ios.rollback()

ios.close()