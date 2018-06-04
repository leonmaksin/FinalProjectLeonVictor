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
data = open(filename,'r').read()
#OPEN FILE

#CLEAN UP
data = data.split('\n')
if '' in data:
    data.remove('')
reference = data[0]
data = data[1:]
for i in range(len(data)):
    data[i] = data[i].split(',')
    data[i] = data[i][:-1]
#CLEAN UP

#HTML STUFF
header = '''<!DOCTYPE html>
<html>
  <head>
    <title>Music!</title>
  </head>
  <body>
    <form class="button" action="home.html" method="post">'''

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

    item_chosen = 'Error'
    if 'choose_number' in form:
        item_chosen = form['choose_number']

    item_type = 'Error'
    if 'item_type' in form:
        item_type = int(form['item_type'])

    error_message = 'Error, please input an integer between 1 and 5000'

    tableData = makeRows(item_chosen,item_type)

    tableHTML(tableData)

def makeRows(song,gatherdex):
    row = []
    #NUMBER
    if gatherdex == -1:
        dict01 = {}
        for i in range(len(data)):
            dict01[str(i+1)] = [i]
        index = dict01[song]
        row = []
        for item in index:
            row.append(data[item])
        return row
    #NUMBER

    #RANK
    if gatherdex == 0:
        dict0 = {}
        for i in range(len(data)):
            item = (data[i])[0]
            item = item.strip('"')
            if item in dict0:
                dict0[item].append(i)
            else:
                dict0[item] = [i]
        index = dict0[song]
        row = []
        for item in index:
            row.append(data[item])
        return row
    #RANK

    #NAME
    if gatherdex == 1:
        dict1 = {}
        for i in range(len(data)):
            item = (data[i])[1]
            item = item.strip('"')
            if item in dict1:
                dict1[item].append(i)
            else:
                dict1[item] = [i]
        index = dict1[song]
        row = []
        for item in index:
            row.append(data[item])
        return row
    #NAME

    #ARTIST
    if gatherdex == 2:
        dict2 = {}
        for i in range(len(data)):
            item = (data[i])[2]
            item = item.strip('"')
            if item in dict2:
                dict2[item].append(i)
            else:
                dict2[item] = [i]
        index = dict2[song]
        row = []
        for item in index:
            row.append(data[item])
        return row
    #ARTIST

    #YEAR
    if gatherdex == 3:
        dict3 = {}
        for i in range(len(data)):
            item = (data[i])[3]
            item = item.strip('"')
            if item in dict3:
                dict3[item].append(i)
            else:
                dict3[item] = [i]
        index = dict3[song]
        row = []
        for item in index:
            row.append(data[item])
        return row
    #YEAR
#MAIN BODY

def tableHTML(data):
    print '    <table border=1>'
    for row in data:
        print '      <tr>'
        for item in row:
            print '<td>' + item + '</td>'
        print '      </tr>'
    print '    </table>'

print header
main()
print foot
