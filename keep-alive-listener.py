#!/usr/bin/python3
import socket
import sys

def main():
    ip, udp_port = sys.argv[1], int(sys.argv[2])
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind((ip, udp_port))
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("Received message:", data)
    return 0

if __name__ == '__main__':
    exit(main())