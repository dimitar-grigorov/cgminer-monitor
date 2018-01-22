#!/usr/bin/python
import argparse
import os
import sys
sys.path.append(os.getcwd())
import pycgminer

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--host')
    parser.add_argument('-p', '--port')
    parser.add_argument('-r', '--rate')
    args = parser.parse_args()

myHost = args.host
myPort = args.port

#print "Connecting to {host} on port {port}".format(host=myHost,port=4028)
cgminer = cgapi.CgminerAPI()
cgminer.host = myHost
cgminer.port = int(myPort)
summary = cgminer.command('summary')
secrate = summary[unicode('SUMMARY')][0][unicode('MHS 5s')]
print secrate

#if secrate < args.rate:
#    exit(1)
#else:
#    exit(0)
