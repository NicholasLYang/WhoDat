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
        return hits
    else: #if the Google API did not return any results (most likely due to too many requests)
        return False
			
