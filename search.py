from urllib2 import urlopen, Request
from urllib import urlencode
import json
from bs4 import BeautifulSoup
import regex
import re

def urls(userquery):
    '''Returns the top four URLs for any Google query.

    Takes a string as a search query.

    Uses the Google API to find results for the search query.
    Adapted from a StackOverflow answer posted by Alex Martelli.
    '''
    query = urlencode({'q': userquery})
    #print query
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
    search_response = urlopen(url)
    search_results = search_response.read()
    results = json.loads(search_results)
    data = results['responseData']
    #print 'Total results: %s' % data['cursor']['estimatedResultCount']
    if data: #if the Google API works fine and returns at least one result
        hits = data['results']
        goodurls = []
        for i in hits:
            goodurls.append(i['url'])
        return goodurls
    else: #if the Google API did not return any results (most likely due to too many requests)
        return False
    #for h in hits: print ' ', h['url']
    #print 'For more results, see %s' % data['cursor']['moreResultsUrl']
    if hits:
        request = Request(hits[0]['url'])
        page = urlopen(request).read()
        soup = BeautifulSoup(page, 'html.parser')
        #soup.get_text().encode("utf8")
        nameresult = regex.name.search(soup.get_text().encode("utf8"))
        startind = 0
        if nameresult:
            words = open('wordlist.txt', 'r').read()
            x = str("\n"+nameresult.group(0).split(" ")[0]+"\n").lower()
            #print x
            print x in words
            while x in words:
                firstval = True
                for m in re.finditer(nameresult.group(0), soup.get_text().encode("utf8")): 
                    if firstval:
                        startind = m.start()
                        firstval = False
                        print "length is " + str(startind+len(nameresult.group(0)))
                        print "Startind is :" + str(startind) + " This is: " + str(nameresult.group(0) in str(soup.get_text().encode("utf8"))[startind+len(nameresult.group(0)):])
                nameresult = regex.name.search(str(soup.get_text().encode("utf8"))[startind+len(nameresult.group(0)):])
                x = str("\n"+nameresult.group(0).split(" ")[0]+"\n").lower()
                print "x is: " + x
                print "x in words is: " + str(x in words)
            print nameresult.group(0)
            print startind
			
urls('Who invented the car?')
words = open('wordlist.txt', 'r').read().split("\n")
#print words[0]