# About The Project
**Network Automation** has been the name of the game, in past couple of decades. With techologies like **Software Defined Networking(SDN)** and **Intent Based Networking(IBN)** being used widespreadly in the industry today, this project is a small effort towards understandig Network Programmability and Automation using Python. All the modules used in this project have been explained below;

# Contents
* [Handling CSV Files](#1-handling-csv-files)
* [Data Serialization and Deserialization](#2-data-serialization-and-deserialization)
    * [Json](#json)
    * [Pickle](#pickle)
* [Serial/Console Connection](#3-serialconsole-connection)
* [Network Automation With](#4-network-automation-with)
    * [Telnet](#telnet)
    * [Paramiko](#paramiko)
    * [Netmiko](#netmiko)
    * [NAPALM](#napalm)
* [Multiprocessing and Multithreading](#5-multiprocessing-and-multithreading)
* [Ansible Automation](#6-ansible-automation)
    * [Ansible Playbooks](#ansible-playbooks)

## 1. Handling CSV Files
In [CSV](https://github.com/sapkotajeevan/pynetwork-automation/tree/master/CSV)
   * **Library Used :** `csv`
   * `randomcsv.csv` represents number of flight records per year. `readfile.py` reads this csv file, converts it into dictionary, and prints out the year in which maximum number of flights happened
## 2. Data Serialization and Deserialization
## JSON
In [JSON](https://github.com/sapkotajeevan/pynetwork-automation/tree/master/JSON)
   * **Library Used :** `json` `requests`
   * `Serialization.py` is a simple script that converts python object into json object, and reverse operation is done by `Deserialize.py` module.
   * `Assignment.py` makes an API call to fetch a json file, serializes into python object, and prints the only elements with **completed:true**
## Pickle
In [Pickle](https://github.com/sapkotajeevan/pynetwork-automation/tree/master/Pickle)
   * **Library Used :** `pickle`
   * `dataserialization_pickle.py` serializes python object into binary object, and outputs `friends.dat` binary file. Reverse operation is also achieved and printed in the CLI
## 3. Serial/Console Connection
In [Serial_Conn](https://github.com/sapkotajeevan/pynetwork-automation/tree/master/Serial_Conn)
   * **Library Used :** `serial` `time`
   * `config.txt` has the commands to be run over Console connection.
   * `myserial.py` is a refactored serial module that has different console operation related definitions such as opening console, running command in console, reading from console and checking initial configuration dialog from console.
   * `Console.py` uses `myserial.py` module, reads configuration from `config.txt` and deploys it over the device via console port
## 4. Network Automation With
## Telnet
In [Telnet_Conn](https://github.com/sapkotajeevan/pynetwork-automation/tree/master/Telnet_Conn)
   * **Library Used :** `telnetlib` `getpass`
   * `devices.txt` contains device IP list in which Telnet session is to be initiated
   * `telnet.py` establishes telnet connection and authenticate credentials respectively. Once session is established interface loopback configurations are pushed via telnet object
## Paramiko
In [Paramiko](https://github.com/sapkotajeevan/pynetwork-automation/tree/master/Paramiko)
   * **Library Used :** `paramiko` `time` `scp`
   * `invokeshell.py` utilizes **SSHClient()** function from paramiko to initiate SSH connection to a device, and sends loopback and ospf related configurations via ssh object
   * `linuxssh.py` is similar to `invokeshell.py`, the only difference being it sends command to linux device using ssh object
   * `myparamiko.py` is a refactored module of paramiko where different definitions such as initiating ssh connection, getting ssh shell, sending command over ssh, and closing ssh connection is defined
   * `routerconfigbackup.py` uses refactored `myparamiko.py` module to take configuration backup of the device and save it in the directory `Directory` including timestamps
   * `scpclient` performs a simple operation of securely copying files to and from another Linux Instance
## Netmiko
## NAPALM
## 5. Multiprocessing and Multithreading
## 6. Ansible Automation
## Ansible Playbooks


# CREDITS
**Prof. Andrei Dumitrscu** for his brilliant course **Master Network Automation with Python for Network Engineers** frorm which references have been taken to come up with this project

# LICENSE
[Terms and Conditions](https://github.com/sapkotajeevan/pynetwork-automation/blob/master/LICENSE)
