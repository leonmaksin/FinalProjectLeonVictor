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
data = data[1:]
for i in range(len(data)):
    data[i] = data[i].split(',')
    data[i] = data[i][:-1]
    for h in range(len(data[i])):
        data[i][h] = data[i][h].strip('"')
#CLEAN UP

#HTML STUFF
header = '''<!DOCTYPE html>
<html>
  <head>
    <title>Music!</title>
    <link rel="stylesheet" href="styletable.css">
  </head>
  <body>
    <form class="" action="home.html" method="post">
      <input type="submit" name="gohome" value="Home">
    </form>
    <br>'''

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

    error_message1 = 'Error, please input a value'
    error_message2 = 'Error, please input a different value'

    if item_chosen == 'Error' or item_type == 'Error':
        print '    <h1>' + error_message1 + '</h1>'
    else:
        item_chosen = item_chosen.lower()
        tableData = makeRows(item_chosen,item_type)
        if tableData == 'Error':
            print '    <h1>' + error_message2 + '</h1>'
        else:
            tableData = manipulateData(tableData)
            tableHTML(tableData)

def manipulateData(tData):
    for i in range(len(tData)):
        name = (tData[i][1]).split()
        tData[i][1] = ''
        for part in name:
            tData[i][1] += part[0].upper() + part[1:] + ' '
        artist = (tData[i][2]).split()
        tData[i][2] = ''
        for part in artist:
            tData[i][2] += part[0].upper() + part[1:] + ' '
        areLyrics = True
        lyrics = tData[i][4]
        if lyrics == 'NA' or lyrics == '':
            tData[i][4] = 'No Lyrics Available'
            areLyrics = False
        if areLyrics:
            lyrics = lyrics.split()
            lyricsDict = {}
            for word in lyrics:
                if word in lyricsDict:
                    lyricsDict[word] += 1
                else:
                    lyricsDict[word] = 1
            tData[i] = tData[i][:4]
            tData[i].append(str(len(lyrics)))
            tData[i].append(str(len(lyricsDict)))
    return tData

def makeRows(song,gatherdex):
    row = []
    #NUMBER
    if gatherdex == -1:
        dict01 = {}
        for i in range(len(data)):
            dict01[str(i+1)] = [i]
        index = dict01[song]
        row = []
        if song in dict01:
            for item in index:
                row.append(data[item])
            return row
        else:
            return 'Error'
    #NUMBER

    #RANK
    if gatherdex == 0:
        dict0 = {}
        for i in range(len(data)):
            item = (data[i])[0]
            if item in dict0:
                dict0[item].append(i)
            else:
                dict0[item] = [i]
        if song in dict0:
            index = dict0[song]
            row = []
            for item in index:
                row.append(data[item])
            return row
        else:
            return 'Error'
    #RANK

    #NAME
    if gatherdex == 1:
        dict1 = {}
        for i in range(len(data)):
            item = (data[i])[1]
            if item in dict1:
                dict1[item].append(i)
            else:
                dict1[item] = [i]
        if song in dict1:
            index = dict1[song]
            row = []
            for item in index:
                row.append(data[item])
            return row
        else:
            return 'Error'
    #NAME

    #ARTIST
    if gatherdex == 2:
        dict2 = {}
        for i in range(len(data)):
            item = (data[i])[2]
            if item in dict2:
                dict2[item].append(i)
            else:
                dict2[item] = [i]
        if song in dict2:
            index = dict2[song]
            row = []
            for item in index:
                row.append(data[item])
            return row
        else:
            return 'Error'
    #ARTIST

    #YEAR
    if gatherdex == 3:
        dict3 = {}
        for i in range(len(data)):
            item = (data[i])[3]
            if item in dict3:
                dict3[item].append(i)
            else:
                dict3[item] = [i]
        if song in dict3:
            index = dict3[song]
            row = []
            for item in index:
                row.append(data[item])
            return row
        else:
            return 'Error'
    #YEAR
#MAIN BODY

def tableHTML(data):
    print '    <table border=1>'
    print '''      <tr>
        <td>Rank</td>
        <td>Song Name</td>
        <td>Artist</td>
        <td>Year</td>
        <td># Lyrics</td>
        <td># Unique Lyrics</td>
      </tr>'''
    for row in data:
        print '      <tr>'
        for item in row:
            print '<td>' + item + '</td>'
        print '      </tr>'
    print '    </table>'

print header
main()
print foot
