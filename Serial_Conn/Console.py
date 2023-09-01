## MY FIRST AUTOMATION 

## Suppose I received 100 routers and I am asked to do same initial configuration in all of switches, the configuration being as mentioned in config.txt.
## I have created myserial.py module which takes care of opening console connection, writing to console, reading to console and checking initial configuration.
## I have imported myserial.py module and then just wrote a commands to convert information in config.txt into list first and then run those commands over console connection.


import myserial

console = myserial.open_console()
myserial.check_initial_configuration_dialog(console)

with open('config.txt') as f:
    commands = f.readlines()   # Reading all the commands in config.txt as list

for cmd in commands:
    myserial.run_command(console,cmd)

output = myserial.read_from_console(console)
print(output)
