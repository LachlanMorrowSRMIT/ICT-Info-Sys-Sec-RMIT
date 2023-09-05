import os

for a in os.environ:
    print (a, '=', os.getenv(a))

print (os.environ['USER'])