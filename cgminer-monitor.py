#!/usr/bin/python
import argparse
import pycgminer



if __name__ == '__main__':
    modeHelp = "How the output will be formatted. Use either Default or PRTG."
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--host', required=True)
    parser.add_argument('-p', '--port', type=int, default=4028)
    parser.add_argument('-m', '--mode', default="Default", help=modeHelp)
    parser.add_argument('-r', '--min-rate', default=0, type=float, help="Min rate. Use only with --mode=PRTG")
    args = parser.parse_args()

# Store arguments in variable
minerHost = args.host
minerPort = args.port
minRate = float(args.min_rate);
prtgMode = args.mode == "PRTG"

if prtgMode and (minRate == 0):
    print "--min-rate is required to be positive in PRTG mode"
    exit(1)

# Setup API object
cgminer = pycgminer.CgminerAPI()
cgminer.host = minerHost
cgminer.port = int(minerPort)

# All output of the command "summary"
summary = cgminer.command('summary')
hashesPerFive = summary[unicode('SUMMARY')][0].get(unicode('GHS 5s'), None)
hashesPerFive = float(hashesPerFive)
# Is hashes None?
if not hashesPerFive:
    exit(1)

# PRTG mode
if prtgMode:
    if hashesPerFive < minRate:
        print '{0}:ERROR'.format(hashesPerFive)
    else:
        print '{0}:OK'.format(hashesPerFive)
# Default mode
else:
    print hashesPerFive
