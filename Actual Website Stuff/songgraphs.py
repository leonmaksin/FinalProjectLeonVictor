#!/usr/bin/python
print "Content-type: text/html\n"

#these 3 lines are important
#matplotlib allows you to use the graphing tools on a web server
#the Agg line is required to work without a graphical desktop (running on a remote computer)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import cgitb
cgitb.enable()

import cgi

#CGI (Copied from Mr. Konstantinovich)
def cgiFieldStorageToDict(fieldStorage):
    ans = {}
    for key in fieldStorage.keys():
        ans[key] = fieldStorage[key].value
    return ans
#CGI

header = '''<!DOCTYPE html>
<html>
  <head>
    <title>Graphs!</title>
    <link rel="stylesheet" href="stylegraphs.css">
  </head>
  <body>
    <form class="home" action="home.html" method="post">
      <input type="submit" name="gohome" value="Home">
    </form>
    <h1>Graphs</h1>'''

foot = '''  </body>
</html>'''

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def main():
    form = cgiFieldStorageToDict(cgi.FieldStorage())

    rankList = ['Rank']
    for key in form:
        key = key.strip('[]')
        key = key.split(',')
        num = key[0]
        num = num.strip()
        num = num.strip('\'')
        rankList.append(num)
    yearList = ['Year']
    for key in form:
        key = key.strip('[]')
        key = key.split(',')
        num = key[3]
        num = num.strip()
        num = num.strip('\'')
        yearList.append(num)
    lyricNList = ['Number of Lyrics']
    for key in form:
        key = key.strip('[]')
        key = key.split(',')
        num = key[4]
        num = num.strip()
        num = num.strip('\'')
        lyricNList.append(num)
    lyricUnList = ['Number of Unique Lyrics']
    for key in form:
        key = key.strip('[]')
        key = key.split(',')
        num = key[5]
        num = num.strip()
        num = num.strip('\'')
        lyricUnList.append(num)

    graph(yearList,rankList,'year_rank')
    graph(yearList,lyricNList,'year_lyric')
    graph(yearList,lyricUnList,'year_lyricun')
    graph(rankList,lyricNList,'rank_lyric')
    graph(rankList,lyricUnList,'rank_lyricun')
    graph(lyricNList,lyricUnList,'lyric_lyricun')

def graph(xaxis,yaxis,imagename):
    xname = xaxis[0]
    yname = yaxis[0]
    xaxis = xaxis[1:]
    yaxis = yaxis[1:]
    poplist = []
    popcount = 0
    for i in range(len(xaxis)):
        if not RepresentsInt(xaxis[i]):
            poplist.append(i)
    for i in range(len(yaxis)):
        if not RepresentsInt(yaxis[i]):
            poplist.append(i)
    for num in poplist:
        xaxis.pop(num-popcount)
        yaxis.pop(num-popcount)
        popcount += 1
    plt.scatter(xaxis,yaxis)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.savefig('img/' + imagename + '.png')
    plt.clf()
    print '    <img src="img/' + imagename + '.png">'

print header
main()
print foot
