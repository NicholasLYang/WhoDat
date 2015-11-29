import urllib2
from urllib2 import urlopen, Request
from urllib import urlencode
from bs4 import BeautifulSoup
import json, regex, search




def WhoSearch(query):
    hits = search.urls(query)
    request = Request(hits[0]['url'])
    page = urlopen(request).read()
    soup = BeautifulSoup(page, 'html.parser')
    print soup.get_text().encode("utf8")
    nameresult = regex.FindName(soup.get_text().encode("utf8"))
    if nameresult:
        print nameresult.group(0)
    else:
        print 'No result'

def WhenSearch(query):
    hits = search.urls(query)
    request = Request(hits[1]['url'])
    page = urlopen(request).read()
    soup = BeautifulSoup(page, 'html.parser')
    file = open('SoupOutput', 'w')
    file.write(soup.get_text().encode("utf8"))
    # Basically finds action word in query (born, die, etc.)
    action = regex.FindActionInQuery(query)
    # print soup.get_text().encode('utf8')
    # Then from there finds key words related to action word, i.e. born -> birth, birthday, etc.
    keyWords = regex.FindKeyWords(action)
    print "Key Words"
    print keyWords
    searchRange = regex.FindSearchRange(keyWords, soup.get_text().encode("utf8"))
    searchRange = searchRange + regex.FindParentheses(soup.get_text().encode("utf8"))
    dates = []
    for searchText in searchRange:
        print searchText
        dates.append(regex.FindAmericanExtendedDate(searchText))
        dates.append(regex.FindAmericanCondensedDate(searchText))
        dates.append(regex.FindEuropeanExtendedDate(searchText))
    dates = filter(None, dates)
    print dates
    
