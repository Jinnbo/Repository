# mapit.py - launches a map in a
# browser using an address from the command line

import webbrowser, sys
import pyperclip


# If ther are arguments, use args as address
# If there are no arguments, grab from clipboard
if len(sys.argv) >1:
    address = " ".join(sys.argv[1:])
    prefix = "https://www.google.com/maps/place/"

    webbrowser.open(prefix + address)

else:
    address = pyperclip.paste()
    webbrowser.open()


# TODO: Get the address from the clipboard
# If there are no arguments, grab from clipboard