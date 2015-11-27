from urllib2 import urlopen, Request
from urllib import urlencode
import json
from bs4 import BeautifulSoup
import regex

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
    hits = data['results']
    #print 'Top %d hits:' % len(hits)
    #for h in hits: print ' ', h['url']
    #print 'For more results, see %s' % data['cursor']['moreResultsUrl']
    if hits:
        request = Request(hits[0]['url'])
        page = urlopen(request).read()
        soup = BeautifulSoup(page, 'html.parser')
        #soup.get_text().encode("utf8")
        nameresult = regex.name.search(soup.get_text().encode("utf8"))
        if nameresult:
            print nameresult.group(0)
		
urls('Who played Spiderman?')