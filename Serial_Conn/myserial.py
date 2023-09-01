import serial
import time

# First we need to open the console. 'console' is the serial object created for information about console interface
def open_console(port='/dev/ttyUSB0',baudrate=9600):
    console = serial.Serial(port='/dev/ttyUSB0',baudrate=9600,parity='N',stopbits=1,bytesize=8,timeout=8)
    if console.isOpen():
        return console
    else:
        return False

# To send command to console interface
def run_command(console,cmd='\n',sleep=1):
    print('Sending command:' + cmd)
    console.write(cmd.encode() + b'\n')
    time.sleep(sleep)

# To read information from console
def read_from_console(console):
    bytes_to_be_read = console.inWaiting()
    if bytes_to_be_read:
        output = console.read(bytes_to_be_read)
        return output.decode()
    else:
        return False

# To check initial configuration dialog. Note you must think of every steps how the switch or router would boot and makes changes in code as username
def check_initial_configuration_dialog(console):
    run_command(console,'\n')
    prompt = read_from_console(console)
    if 'Would you like to enter the initial configuration dialog?' in prompt:
        run_command(console,'no',15)
        run_command(console,'\r\n')
        return True
    else:
        return False
