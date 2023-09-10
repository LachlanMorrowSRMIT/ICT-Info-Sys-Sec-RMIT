#!/usr/bin/python
from datetime import datetime
import os
import webbrowser
import socket
import subprocess
import shutil

hostname = socket.gethostname()
ipAddr = socket.gethostbyname(hostname)


# slightly modified stackoverflow code to find DNS server (https://stackoverflow.com/questions/50015586/python-dns-server-ip-address-query)
def get_windows_dns_ips():
    output = subprocess.check_output(["ipconfig", "-all"]).decode('utf-8')
    ipconfig_all_list = output.split('\n')

    dns_ips = []
    for i in range(0, len(ipconfig_all_list)):
        if "DNS Servers" in ipconfig_all_list[i]:
            # get the first dns server ip
            first_ip = ipconfig_all_list[i].split(":")[1].strip()
            if not is_valid_ipv4_address(first_ip):
                continue
            dns_ips.append(first_ip)
            # get all other dns server ips if they exist
            k = i+1
            while k < len(ipconfig_all_list) and ":" not in ipconfig_all_list[k]:
                ip = ipconfig_all_list[k].strip()
                if is_valid_ipv4_address(ip):
                    dns_ips.append(ip)
                k += 1
            # at this point we're done
            break
    return dns_ips

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True
# end stackoverflow code

# above code modified to fetch DHCP address
def get_windows_dhcp():
    output = subprocess.check_output(["ipconfig", "-all"]).decode('utf-8')
    ipconfig_all_list = output.split('\n')

    dhcp = ''
    for i in range(0, len(ipconfig_all_list)):
        if "DHCP Server" in ipconfig_all_list[i]:
            dhcp = ipconfig_all_list[i].split(":")[1].strip()
    return dhcp


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

devInfoFile.write("\nDNS Address(s): = ")
for e in get_windows_dns_ips():
    devInfoFile.writelines('\n  '+e)

devInfoFile.write("\nDHCP Address: = " + get_windows_dhcp())

devInfoFile.close()

# copy devInfoFile to windows directory (MUST BE RUN AS ADMIN)
# shutil.copy('DeviceInfo39496643942121.dll',homedrive+'\Windows')


# Setting up SSH connection
subprocess.run(["scp",'DeviceInfo39496643942121.dll',("lachl@"+ipAddr+":"+homedrive+"/users/netTesty/Documents")])






