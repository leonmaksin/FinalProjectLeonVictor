#!/usr/bin/python
print "Content-type: text/html\n"

#these 3 lines are important
#matplotlib allows you to use the graphing tools on a web server
#the Agg line is required to work without a graphical desktop (running on a remote computer)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

#help you see errors
import cgitb
cgitb.enable()

print "<!DOCTYPE>"
print "<html>"
print "<head>"
print "</head>"
print "<body>"
print "</body>"
print "</html>"
