import json
from bs4 import BeautifulSoup
import regex



'''Returns the top four URLs for any Google query.

    Takes a string as a search query.

    Uses the Google API to find results for the search query.
    Adapted from a StackOverflow answer posted by Alex Martelli.
'''
userquery = "When did John Lennon die"
query = urlencode({'q': userquery})
#print query
url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
search_response = urlopen(url)
search_results = search_response.read()
results = json.loads(search_results)
data = results['responseData']
#print 'Total results: %s' % data['cursor']['estimatedResultCount']
hits = data['results']
print hits