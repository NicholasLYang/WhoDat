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
    # Finds name of person (if applicable) in query
    name = regex.FindName(query)
     print "Name: " + name
    hits = search.urls(query)
    for hit in hits:
        print hit['titleNoFormatting']
        request = Request(hit['url'])
        page = urlopen(request).read()
        soup = BeautifulSoup(page, 'html.parser')
        print regex.FindName(hit['titleNoFormatting'])
        if (regex.FindName(hit['titleNoFormatting']) == name):
            print "found it"
    # Saving the output of beautiful soup for debugging
    file = open('SoupOutput', 'w')
    file.write(soup.get_text().encode("utf8"))
    # Basically finds action word in query (born, die, etc.)
    action = regex.FindActionInQuery(query)
    # Then from there finds key words related to action word, i.e. born -> birth, birthday, etc.
    keyWords = regex.FindKeyWords(action)
    

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

def WhySearch(query):
    return "Why not?"