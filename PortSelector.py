#!/usr/bin/python3

import argparse
import sys
import os

# The list of "top ports" is used from nmap. 
# Change this if your nmap files are located elsewhere
NMAPSERVICEFILE = "/usr/share/nmap/nmap-services"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-range", "-r", help="the range of 'top-ports' to generate, START_PORT_RANK-END_PORT_RANK")
    parser.add_argument("-tcp", "-t", action='store_true', help="output top TCP ports (can't use at same time as UDP)")
    parser.add_argument("-udp", "-u", action='store_true', help="output top UDP ports (can't use at the same time as TCP)")
    parser.add_argument("-setEnvVar", "-s", default="NULL", help="(OPTIONAL) export the ports to the provided environment variable name (i.e., pass to nmap with -p $ENVVAR)")

    args = parser.parse_args()

    # Validate arguments
    if not args.range or (not args.tcp and not args.udp):
        parser.print_help()
        sys.exit(1)

    startRank, endRank = map(int, args.range.split('-'))

    if startRank >= endRank or endRank > 3000:
        print("Invalid port range.")
        sys.exit(1)

    # Initialize lists
    protocolLines = []
    sortedLines = []
    subsetList = []

    # Read the services
    with open(NMAPSERVICEFILE, 'r') as nmap_file:
        for line in nmap_file:
            
            if line.startswith('#'):
                continue

            if args.tcp and "/tcp" in line:
                protocolLines.append(line)

            if args.udp and "/udp" in line:
                protocolLines.append(line)

    # Sort by open-frequency column
    sortedLines = sorted(protocolLines, key=lambda line: int(line.split()[2]), reverse=True)

    # Create subset list
    index = startRank - 1
    while index < endRank:
        subsetList.append(sortedLines[index])
        index += 1

    portString = ",".join(line.split()[1].split("/")[0] for line in subsetList)

    # Output the selected ports
    if args.tcp:
        print(f"Top {startRank} to {endRank} TCP services:")
    elif args.udp:
        print(f"Top {startRank} to {endRank} UDP services:")
    
    print(portString)

    # Check if we need to export an environmental variable
    if args.setEnvVar != "NULL":
        print(f"Ports exported to environmental variable: {args.setEnvVar}")
        print(f"Use with nmap, etc., like: nmap -p ${args.setEnvVar}")
        print("Type 'exit' after running nmap to return to your original bash context")
        os.putenv(args.setEnvVar, portString)
        os.system('bash')

if __name__ == '__main__':
    main()
