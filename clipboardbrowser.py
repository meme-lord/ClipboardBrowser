from sys import argv
from win10toast import ToastNotifier
from pyperclip import copy
copy(argv[1])
toaster = ToastNotifier()
toaster.show_toast("URL added to clipboard","URL: %s" % argv[1])
