#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

fs = cgi.FieldStorage()
c = fs.getvalue("input")
op = subprocess.getoutput("sudo " + c)
print(op)
