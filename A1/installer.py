#!/usr/bin/python
import os
file = open("information.txt", "w")

for a in os.environ:
    file.writelines(a + '=' + os.getenv(a))
    file.writelines("\n")
    if a == os.getenv('USER'):
        username = a

file.writelines("\n")
file.writelines(a)
file.close()
