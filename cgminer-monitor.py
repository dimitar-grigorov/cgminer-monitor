#!/usr/bin/env python3
import argparse
import pycgminer

# Entry point of the script
if __name__ == '__main__':
    # Help text for mode argument
    modeHelp = "How the output will be formatted. Use either Default or PRTG."
    
    # Initialize argument parser
    parser = argparse.ArgumentParser()
    
    # Define script arguments
    parser.add_argument('-a', '--host', required=True)
    parser.add_argument('-p', '--port', type=int, default=4028)
    parser.add_argument('-m', '--mode', default="Default", help=modeHelp)
    parser.add_argument('-r', '--min-rate', default=0, type=float, help="Min rate. Use only with --mode=PRTG")
    
    # Parse arguments
    args = parser.parse_args()

# Store parsed arguments in variables
minerHost = args.host
minerPort = args.port
minRate = float(args.min_rate)
prtgMode = args.mode == "PRTG"

# Check if min-rate is positive when in PRTG mode
if prtgMode and (minRate == 0):
    print("--min-rate is required to be positive in PRTG mode")
    exit(1)

# Initialize CgminerAPI object
cgminer = pycgminer.CgminerAPI()
cgminer.host = minerHost
cgminer.port = int(minerPort)

# Get summary from cgminer
summary = cgminer.command('summary')
hashesPerFive = summary[str('SUMMARY')][0].get(str('GHS 5s'), None)
hashesPerFive = float(hashesPerFive)

# Check if hashesPerFive is None
if not hashesPerFive:
    exit(1)

# Output formatting for PRTG mode
if prtgMode:
    if hashesPerFive < minRate:
        print('{0}:ERROR'.format(hashesPerFive))
    else:
        print('{0}:OK'.format(hashesPerFive))
# Output formatting for Default mode
else:
    print(hashesPerFive)