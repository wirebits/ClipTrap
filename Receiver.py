# ClipTrap
# A tool which copy text to the clipboard remotely.
# Author - WireBits

# Receiver Code

import sys
import socket
import pyperclip as pc

HOST = '0.0.0.0'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            received_text = data.decode()
            pc.copy(received_text)