#!/usr/bin/env python3
import argparse
import pycgminer

# Help text for mode argument
MODE_HELP = "How the output will be formatted. Use either Default or PRTG."

# Initialize argument parser
parser = argparse.ArgumentParser()

# Define script arguments
parser.add_argument('-a', '--host', required=True, help="Miner host address")
parser.add_argument('-p', '--port', type=int, default=4028, help="Miner port (default: 4028)")
parser.add_argument('-m', '--mode', default="Default", help=MODE_HELP)
parser.add_argument('-r', '--min-rate', default=0, type=float, help="Min rate. Use only with --mode=PRTG")

# Parse arguments
args = parser.parse_args()

# Store parsed arguments in variables
miner_host = args.host
miner_port = args.port
min_rate = float(args.min_rate)
prtg_mode = args.mode == "PRTG"

# Check if min-rate is positive when in PRTG mode
if prtg_mode and min_rate <= 0:
    print("--min-rate is required to be positive in PRTG mode")
    exit(1)

# Initialize CgminerAPI object
cgminer = pycgminer.CgminerAPI()
cgminer.host = miner_host
cgminer.port = int(miner_port)

# Get summary from cgminer
summary = cgminer.command('summary')
# hashesPerFive = summary[unicode('SUMMARY')][0].get(unicode('GHS 5s'), None)
hashes_per_five = summary.get('SUMMARY', [{}])[0].get('GHS 5s', None)
hashes_per_five = float(hashes_per_five) if hashes_per_five else None

# Check if hashes_per_five is None
if hashes_per_five is None:
    exit(1)

# Output formatting for PRTG mode
if prtg_mode:
    if hashes_per_five < min_rate:
        print(f'{hashes_per_five}:ERROR')
    else:
        print(f'{hashes_per_five}:OK')
# Output formatting for Default mode
else:
    print(hashes_per_five)
