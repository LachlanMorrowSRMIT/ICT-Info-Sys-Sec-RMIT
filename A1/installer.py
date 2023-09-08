#!/usr/bin/python
from datetime import datetime
import os
import webbrowser
import socket
import platform
import subprocess

hostname = socket.gethostname()
ipAddr = socket.gethostbyname(hostname)

tFile = open("text file.txt", "w")

# write System Time
tFile.write("System Time: "+str(datetime.now()) + "\n")

# write student numbers
tFile.write("Student 1 (Manav) Number: s3949664 \nStudent 2 (Lachlan) Number: s3942121\n")

# Open URL (google)
# webbrowser.open("http://www.google.com")

# Write username
tFile.writelines("\nCurrent User: "+ str(os.getlogin()))


# Close text file
tFile.close()

devInfoFile = open("DeviceInfo39496643942121.dll", "w")

for a in os.environ:
    devInfoFile.writelines(a+ '='+ os.getenv(a)+"\n")
    if(str(a) == "HOMEDRIVE"):
        homedrive = os.getenv(a)
devInfoFile.write("\n\nHome Drive = "+ homedrive)

devInfoFile.write("\nIP Address: = "+ ipAddr)


os.system("git clone https://github.com/rthalley/dnspython.git")


devInfoFile.close()



