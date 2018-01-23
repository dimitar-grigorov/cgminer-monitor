#!/usr/bin/python
import argparse
# import os
# import sys
# sys.path.append(os.getcwd())
import pycgminer

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--host', required=True)
    parser.add_argument('-p', '--port', type=int, default=4028)
    # parser.add_argument('-r', '--rate')
    args = parser.parse_args()

myHost = args.host
myPort = args.port

# print "Connecting to {host} on port {port}".format(host=myHost,port=4028)
cgminer = pycgminer.CgminerAPI()
cgminer.host = myHost
cgminer.port = int(myPort)

summary = cgminer.command('summary')
secrate = summary[unicode('SUMMARY')][0].get(unicode('GHS 5s'), None)

# Is None?
if not secrate:
    exit(1)

print secrate

# if secrate < args.rate:
#     exit(1)
# else:
#     exit(0)
