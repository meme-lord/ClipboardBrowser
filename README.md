# Clipboard Browser
Basically instead of opening links in my browser I wanted to just copy them to my clipboard so I could choose what to do with it.
The scripts in this repo allow me to do that.

# Installation
Clone this repo to `C:\Program Files\ClipboardBrowser\` or edit the install.reg as needed.

Install the required python libraries (`python -m pip install win10toast pyperclip`) and change the pythonw.exe path in the install.reg to the location of your Python installation.

Run install.reg, this will add the script to the registry as a web browser.

Change your default browser to "python" or "clipboardbrowser" in Windows settings or change the http, https URL handler.
