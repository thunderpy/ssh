# Python script to access Switch
import os

switchNames = {

    "VH1": "user@192.168.1.1",

    "VH2": "user@192.168.1.2"
}

for k, v in switchNames.items():
    print(k, end=', ')

print('\n')
switchSelected = input("Enter Floor name as above: ").upper()

if switchSelected not in switchNames.keys():
    print("Invalid " + switchSelected + " not in dictionary!!!!")
else:
    print("Accessing " + switchSelected + " switch....")

    # use os module to run system commands.
    st = "ssh "
    ip = str(switchNames[switchSelected])
    print(st + ip)
    
    os.system(st + ip)
    

