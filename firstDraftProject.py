#!/usr/bin/python
print "Content-type: text/html\n"

import cgitb
cgitb.enable()

import cgi

import string

#CGI (Copied from Mr. Konstantinovich)
def cgiFieldStorageToDict(fieldStorage):
    ans = {}
    for key in fieldStorage.keys():
        ans[key] = fieldStorage[key].value
    return ans
#CGI

#OPEN FILE
filename = '5101 - billboard_lyrics_1964-2015.csv'
text = open(filename,'r').read()
#OPEN FILE

#CLEAN UP
text = text.split('\n')
reference = text[0]
text = text[1:]
#

#HTML STUFF
header = '''<!DOCTYPE html>
<html>
  <head>
    <title>Music!</title>
  </head>
  <body>'''

foot = '''  </body> 
</html>'''
#HTML STUFF

#MAIN BODY
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def main():
    form = cgiFieldStorageToDict(cgi.FieldStorage())

    last = "this is an example for getting data"
    if "example" in form:
        last = form["example"]

    song_chosen = 'Error'
    if 'choose_number' in form:
        song_chosen = form['choose_number']

    error_message = 'Error, please input an integer between 1 and 5000'

    if RepresentsInt(song_chosen):
        song_chosen = int(song_chosen)
        if song_chosen > 5000:
            print '    <p>' + error_message + '</p>'
        else:
            print '    <p>' + text[song_chosen] + '</p>'
    else:
        print '    <p>' + error_message + '</p>'
#MAIN BODY

print header
main()
print foot

