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
    nameresult = regex.FindName(soup.get_text().encode("utf8"))
    if nameresult:
        print nameresult.group(0)
    else:
        print 'No result'

WhoSearch("Who played spiderman")