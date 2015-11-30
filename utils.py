
import urllib2, bs4, re, search, regex, os


def WhereSearch(query):
    results = google.search(query, num = 3, start = 0, stop = 10)
    
    resultList = []
    for result in results:
        url = urllib2.request.urlopen(result)
        page = url.read()
        soup = bs4.BeautifulSoup(page, 'html.parser')
    print soup.title
	
def WhoSearch(query):
    hits = search.urls(query)
    if hits:
        results = []
        for i in hits:
            results.append(i['url'])
        #results is now a list containing URLs for the top (usually 4) Google search results for the Who query.
        page = urllib2.urlopen(results[0]).read() #may later add code to read other URLs as well
        soup = bs4.BeautifulSoup(page, 'html.parser') #BeautifulSoup parsing of URL of first Google result
        pagetext = soup.get_text().encode("utf8")
        nameresult = regex.name.search(pagetext) #first potential "name" match within the BeautifulSoup text.
        if nameresult: #if there is a match for a potential "name", let's check to make sure it's actually a name.
            #startind = 0
            print nameresult.group(0) #prints potential match
            os.chdir(r'C:\Users\Mastermind\WhoDat')
            words = open('wordsEn.txt', 'r').read()
            names = open('first-names-female.txt', 'r').read() + open('first-names-male.txt', 'r').read()
            name1words = str("\n"+nameresult.group(0).split(" ")[0]+"\n").lower()
            name2words = str("\n"+nameresult.group(0).split(" ")[1]+"\n").lower()
            name1names = str("\n"+nameresult.group(0).split(" ")[0]+"\n")
            name2names = str("\n"+nameresult.group(0).split(" ")[1]+"\n")
            #print "First name in words: " + str(name1words in words)
            #print "First name in names: " + str(name1names in names)
            #the purpose of this next loop is to skip false positives until it finds a result where the first two parts of the name are NOT [in words and not in names]
            while ((name1words in words) and not (name1names in names)) or ((name2words in words) and not (name2names in names)):
                pagetext = pagetext[(pagetext.find(nameresult.group(0))+len(nameresult.group(0).split(" ")[0])):] #deletes everything up to (and including) the first word of the current false positive.
                #print "length is: " + str(startind+len(nameresult.group(0)))
                #print "nameresult.group(0) is: " + str(nameresult.group(0))
                #print "Startind is: " + str(startind) + " Found in rest of text?: " + str(nameresult.group(0) in pagetext[startind+len(nameresult.group(0)):])
                nameresult = regex.name.search(pagetext)
                #print "The current name being considered is: " + str(nameresult.group(0))
                name1words = str("\n"+nameresult.group(0).split(" ")[0]+"\n").lower()
                name2words = str("\n"+nameresult.group(0).split(" ")[1]+"\n").lower()
                name1names = str("\n"+nameresult.group(0).split(" ")[0]+"\n")
                name2names = str("\n"+nameresult.group(0).split(" ")[1]+"\n")
                #print "First name: " + nameresult.group(0).split(" ")[0]
                #print "First name in names: " + str(name1names in names)
                #print "First name in words: " + str(name1words in words)
                #print "second name: " + nameresult.group(0).split(" ")[1]
                #print "second name in names: " + str(name2names in names)
                #print "second name in words: " + str(name2words in words)
                #print "________________"
            return nameresult.group(0)
    else:
	    return "An error occurred: No results found. If Googling your query returns results, please wait a while and try entering it here again."
    #for i in results:
    #    print i

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
	
#while(True):
#    userinput = raw_input('What would you like to search for? ')
#    WhoSearch(str(userinput))
	
	
#print "Who invented the stapler?"
#WhoSearch("Who invented the stapler?")

#print "Who discovered America?"
#WhoSearch("Who discovered America?")

#print "Who created the Atmoic Bomb?"
#WhoSearch("Who created the Atmoic Bomb?")