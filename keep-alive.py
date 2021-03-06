#!/usr/bin/python3

# ./keep-alive.py remote_address timeout rem_port local_port1 local_port2 local_portN
# количество локальных портов на которых мы открываем сокет - переменное
# timeout - задержка между пакетами
# с каждого сокета мы посылаем
# UDP 0
# ну пусть будет CRLF
# 0x0D  0x0A  0x0D  0x0A   
# Да бесконечный цикл, - таймаут в секундах

import socket
import sys
import time
from datetime import datetime
from threading import Thread

DATA = "0x0D 0x0A 0x0D 0x0A"

def parse_input(argv):
    rem_ip, timeout, rem_port = argv[1], int(argv[2]), int(argv[3])
    local_ports = []
    for arg in argv[4:]:
        local_ports.append(int(arg))
    return rem_ip, timeout, rem_port, local_ports

def send_data(rem_ip, timeout, rem_port, local_port):
    # create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # bind socket to a local port
    sock.bind(('', local_port))
    while True:
        sock.sendto(bytes(DATA, "utf-8"), (rem_ip, rem_port))
        print("Packet is sent to " + rem_ip + ":" + str(rem_port) + " at " + str(datetime.now()) + " (from UDP port: " + str(local_port) + ")")
        time.sleep(timeout)

def main():
    argv = sys.argv
    try:
        assert len(argv) >= 5, "Script usage: " + __file__ + " remote_ip timeout remote_port local_port1 local_port2 ... local_portN"
        # get remote_address, timeout and local_ports from script arguments
        rem_ip, timeout, rem_port, local_ports = parse_input(sys.argv)
        # create a thread for every local port in the list
        for local_port in local_ports:
            Thread(target=send_data, args=(rem_ip, timeout, rem_port, local_port)).start()
    except (AssertionError) as e:
        print(e)
        return 1
    return 0

if __name__ == '__main__':
    exit(main())
