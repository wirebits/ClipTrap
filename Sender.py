# ClipTrap
# A tool which copy text to the clipboard remotely.
# Author - WireBits

# Sender Code

import sys
import socket

HOST = 'Victim IP Address'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        text_to_send = input("Enter text to send (or type 'exit' to quit): ")
        if text_to_send.lower() == 'exit':
            break

        s.sendall(text_to_send.encode())