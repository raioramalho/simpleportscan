#!/usr/bin/env python3

# This script will check if port is open or not
#
# Author: Alan Ramalho
# Date: 11/03/2022
# Version: 1.0

def scan():
    import socket
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Port Scanner')
    parser.add_argument('-H', '--host', type=str, help='Host to scan')
    parser.add_argument('-p', '--port', type=int, help='Port to scan')
    args = parser.parse_args()

    if args.host is None:
        print('[-] Please specify a host to scan')
        sys.exit(0)
    if args.port is None:
        print('[-] Please specify a port to scan')
        sys.exit(0)

    host = args.host
    port = args.port

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect((host, port))
        s.close()
        print('[+] Port {} is open'.format(port))
    except:
        print('[-] Port {} is closed'.format(port))

scan()
