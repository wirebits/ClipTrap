# ClipTrap
# A tool which copy text to the clipboard.
# Author - WireBits

import sys
import pyperclip as pc

text = input("Enter your text: ")
pc.copy(text)

clipboard_text = pc.paste()
if not clipboard_text:
    sys.exit()