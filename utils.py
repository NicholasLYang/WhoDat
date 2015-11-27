import google, urllib2, bs4, re

def WhereSearch(query):
    results = google.search(query, num = 3, start = 0, stop = 10)
    
    resultList = []
    for result in results:
        url = urllib2.request.urlopen(result)
        page = url.read()
        soup = bs4.BeautifulSoup(page, 'html.parser')
    print soup.title