import myparamiko

devices = ['10.10.10.1','10.10.10.2','10.10.10.3']

for device in devices:
    ssh_client = myparamiko.connect(device,22,'jeevan','cisco')
    remote_connection = myparamiko.get_shell(ssh_client)
    myparamiko.send_command(remote_connection,'enable')
    myparamiko.send_command(remote_connection,'cisco')
    myparamiko.send_command(remote_connection,'terminal length 0')
    output = myparamiko.send_command(remote_connection,'show run')

    output_str = output.decode()

    list = output_str.split('\n')
    list = list[4:-1]
    config = '\n'.join(list)

    import datetime
    now = datetime.datetime.now()
    today = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    file = device + '-' + today + '.txt'

    with open(file,'w') as f:
        print('Saving Configuration of' + device)
        f.write(config)
        print('OK')

    myparamiko.close(ssh_client)
