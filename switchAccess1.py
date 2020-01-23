# Python script to access NW18 Switch
import paramiko

switchNames = {

    "VH1": "192.168.101.1",

    "VH2": "192.168.101.2"
}

for k, v in switchNames.items():
    print(k, end=', ')

print('\n')
switchSelected = input("Enter Floor name as above: ").upper()

if switchSelected not in switchNames.keys():
    print("Invalid " + switchSelected + " not in dictionary!!!!")
else:
    print("Accessing " + switchSelected + " switch....")

    ip = str(switchNames[switchSelected])
    USER = input("Enter username:- ")
    PASSWORD = input("Enter password:- ")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=USER, password=PASSWORD)





