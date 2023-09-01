from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret':'cisco'}
ios = driver('10.10.10.40','admin','cisco',optional_args = optional_args)

ios.open()

ios.load_merge_candidate(filename='configadd.txt')
diff = ios.compare_config()
if len(diff)>0:
    print(diff)
    answer = input('Commit Changes?<yes|no>')
    if answer == 'yes':
        print('Commiting changes...')
        ios.commit_config()
        print('Done')
    else:
        print('No changes required...')
        ios.discard_config()
        # print('Rolling Back Configuration...')
        # ios.rollback()

ios.close()