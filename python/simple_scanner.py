#!/bin/python3

import sys
import socket
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translating a hostname to IPv4
else:
    print("Invalid ammount of arguments.")
    print("python3 scanner.py <ip>")
    sys.exit()

#Add a banner
print("-" * 50)
print(f"Scanning target {target}")
print(f"Time started {str(datetime.now())}")
print("-" * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # if port is not connectable, it timesout at 1 second
        result = s.connect_ex((target,port)) # returns an error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting...")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# improvements: threading