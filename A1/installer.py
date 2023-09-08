#!/usr/bin/python
from datetime import datetime
import os
import webbrowser

tFile = open("information.txt", "w")

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

devInfoFile = open("DeviceInfos3949664s3942121.dll", "w")

for a in os.environ:
    devInfoFile.writelines(a+ '='+ os.getenv(a)+"\n")
    if(str(a) == "HOMEDRIVE"):
        homedrive = a



devInfoFile.close()
