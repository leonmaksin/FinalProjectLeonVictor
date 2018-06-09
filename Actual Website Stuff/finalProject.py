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
    <form class="home" action="finalproject.html" method="post">
      <input type="submit" name="gohome" value="Home">
    </form>'''

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

    checked = ''
    if 'checkedall' in form:
        checked = ' checked'
        valList = form['checkedall'].split(',')
        item_chosen = valList[0]
        item_type = int(valList[1])
    else:
        checked = ''
        item_chosen = 'none'
        if 'choose_number' in form:
            item_chosen = form['choose_number']

        item_type = 'none'
        if 'item_type' in form:
            item_type = int(form['item_type'])

    error_message1 = 'Error, please input a value'
    error_message2 = 'Error, please input a different value'

    item_chosen = item_chosen.lower()
    tableData = makeRows(item_chosen,item_type)
    if tableData == 'Error':
        print '    <h1>' + error_message2 + '</h1>'
    else:
        tableData = manipulateData(tableData)
        tableHTML(tableData,str(item_chosen),str(item_type),checked)

def manipulateData(tData):
    last = tData[-1]
    print '    <p id="results">' + str(last) + ' results found</p>'
    tData.remove(last)
    for i in range(len(tData)):
        name = ((tData[i])[1]).split()
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
            tData[i].append('')
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
    if song == 'none':
        return data + [len(data)]
    row = []
    #NUMBER
    if gatherdex == -1:
        row0 = makeRows(song,0)
        if row0 == 'Error':
            row0 = [0]
        row1 = makeRows(song,1)
        if row1 == 'Error':
            row1 = [0]
        row2 = makeRows(song,2)
        if row2 == 'Error':
            row2 = [0]
        row3 = makeRows(song,3)
        if row3 == 'Error':
            row3 = [0]

        length = row0[-1] + row1[-1] + row2[-1] + row3[-1]
        row0.remove(row0[-1])
        row1.remove(row1[-1])
        row2.remove(row2[-1])
        row3.remove(row3[-1])
        row = row0 + row1 + row2 + row3
        for item in row:
            newRow = []
            newRow += row
            newRow.remove(item)
            if item in newRow:
                row = newRow
        if len(row) == 0:
            return "Error"
        row.append(length)
        return row
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
        index = []
        if song in dict0:
            index = dict0[song]
        row = []
        for item in index:
            row.append(data[item])
        if row != []:
            row.append(len(row))
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
        index = []
        for key in dict1:
            if song in key:
                for num in dict1[key]:
                    index.append(num)
        row = []
        for item in index:
            row.append(data[item])
        if row != []:
            row.append(len(row))
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
        index = []
        for key in dict2:
            if song in key:
                for num in dict2[key]:
                    index.append(num)
        row = []
        for item in index:
            row.append(data[item])
        if row != []:
            row.append(len(row))
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
        index = []
        for key in dict3:
            if song in key:
                for num in dict3[key]:
                    index.append(num)
        row = []
        for item in index:
            row.append(data[item])
        if row != []:
            row.append(len(row))
            return row
        else:
            return 'Error'
    #YEAR
#MAIN BODY

def tableHTML(data,item_chosen,item_type,checked):
    print '    <form class="graph" action="songgraphs.py" method="post">'
    print '    <table border=1>'
    print '''      <tr>
        <td>Rank</td>
        <td>Song Name</td>
        <td>Artist</td>
        <td>Year</td>
        <td># Lyrics</td>
        <td># Unique Lyrics</td>
        <td>Graph?</td>
      </tr>'''
    for row in data:
        print '      <tr>'
        for i in range(len(row)):
            print '        <td>' + row[i] + '</td>'
        print '        <td><input type="checkbox" name="' + str(row).replace('\"','\'') + '"' + checked + '></td>'
        print '      </tr>'
    print '    </table>'
    print '    <br>'
    print '    <input type="submit" value="Compare Checked Songs on Graph">'
    print '    </form>'
    print '    <br>'
    graphbox = '''        <form class="checkall" action="finalProject.py" method="post">
          <input type="hidden" name="checkedall" value="''' + item_chosen + ',' + item_type + '''">
          <input type="submit" name="checkedsubmit" value="Check All" style="font-size:20px">
        </form>'''
    print graphbox

print header
main()
print foot
