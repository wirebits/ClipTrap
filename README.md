# ClipTrap
A tool which copy text to the clipboard remotely.

# Key Features
- Copy text to the clipboard.
- When *Sender.py* closed, then automatically the *Receiver.py* stops.
- If the clipboard is empty, then the program stopped.

# Demo Video

https://github.com/wirebits/ClipTrap/assets/159493381/c0ec7e20-a162-4377-80e8-80e2a6050368

# OS Support
- Windows 10
- Raspberry Pi OS

# Role
- *Raspberry Pi OS* act as Sender Machine (Raspberry Pi Zero W).
- *Windows 10* act as Receiver Machine (Laptop).

# Setup
1. Make sure the latest python and pip3 is installed on your system (Windows/Linux/MacOS).<br>
2. Install the *pyperclip* and *sockets* modules on your system (Windows/Linux/MacOS) by copy and run the following command :<br>

```
pip3 install -r requirements.txt
```

# Install and Run
1. Download or Clone the Repository.
2. Open the folder.
3. After that put the *Victim IP Address* at the indicated place in **Sender.py** file.
4. Run the *Sender.py* file at the Sender Machine.
5. Run the *Receiver.py* file at the Receiver Machine.
6. Wait for few seconds, the *Receiver.py* show a message **Connected by (Sender IP Address)**.
7. Now, we are ready to send text.
8. To run *Receiver.py* file without console window in windows :

```
pythonw.exe Receiver.py
```
# Get Victim IP Address

## Windows
1. Open CMD.
2. Type *ipconfig*.
3. Click Enter.
4. Under the *Wireless LAN adapter Wi-Fi:*, there is a *IPv4 Address* and that is your victim address.

## Linux
1. Open Terminal.
2. Type *ifconfig*.
3. Click Enter.
4. Under the *wlan0*, there is a *inet* and that is your victim address.

# For Faster Execution
Use a USB Rubber Ducky to run *Receiver.py* file using powershell.
