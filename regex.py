import re

#regex.py: A collection of Regex expressions to be used for identifying queries and finding answers.
#
#Who queries (finding a name)
#~~~~~~~~~~~
#Our understanding of what a name "is":
#	Plain English:
#	First name: 
#		It starts with a capital letter
#		If abbreviated as an initial, it only has two characters, the second being a period. (ex. J. K. Rowling)
#		Otherwise, it followed by one or more letters or certain grammatical marks (ex. "-", "'", in "This-Name Containsadashforsomereason, Eli'kai)
#			Generally, first names will not contain dashes. Some names may contain more than one apostrophe. (ex. Ku'oko'a)
#			Names may NOT start or end with dashes. (That is, every dash must exist between two letters.)
#			In rarer cases, names may start or end with apostrophes 
#				ex. `Auli`i, Andre'
#			Capital letters are permissible in the middle of a first name, but should exist between two lowercase letters. (Two consecutive capital letters are never seen in a first name.)
#				ex. AnneMarie
#
#	Middle name(s): 
#		Are OPTIONAL
#		If abbreviated as an initial, it only has two characters, the second being a period. (ex. J. K. Rowling)
#		May start with a capital OR lowercase letter
#			 ex. van ,der, van der , de
#		Otherwise, the same rules apply as for first names.
#
#	Last names:
#		Same rules as for first names, except that they may contain dashes.
#
#Converted to Regex:

# Verbose Regex example only: (IGNORE)
# decimal = re.compile(r"""
#					\d +  # the integral part
#					\.    # the decimal point
#					\d *  # some fractional digits""", re.X)
#			
#print decimal.search("not a decimal at all 3.22 3.23").group(0)
			
#currently only lacking adaptation for names like O'Malley
name = re.compile(r"""
					(											# First name:
					(?:(Mc|O'|de|De|[A-Z])						# starts with capital letter (or special start Mc O' De de etc.)
					([a-z]'|[a-z])+[ ])							# followed dashes surrounded by lowercase letters OR apostrophes following a lowercase letter OR just lowercase letters
					|											# or
					(?:[A-Z]\.[ ])   							# is just an initial
					)
					(											# Middle name(s): (optional)
					(?:(van|der|de|De))
					|
					(?:([a-z]'|[A-Z])							# Same as above, except it can start with lowercase letter
					([a-z][-][A-Z]|[a-z]'|[a-z])+[ ])		
					|						
					(?:[A-Z]\.[ ])   		
					)
					{0,5}										# Allow for up to five middle names
					(											# Last name:
					(?:(Mc|O'|de|De|[A-Z])						# Same as first name
					([a-z][-][A-Z]|[a-z]'|[a-z])+)				# Do NOT require a space at the end (could end in a period, comma, etc.)
					|					
					(?:[A-Z]\.)   		
					)	
					""", re.X)				

#nameresult1 = name.search("Thomas Edison a name not an Arthur C. Clarcke ")
#if nameresult1: print nameresult1.group(0)
#nameresult2 = name.search("This is a normal sentence without any names.")
#if nameresult2: print nameresult2.group(0)
#nameresult3 = name.search("This is a normal sentence with a really weird name: McAnd're van 'tala D. C. AnneMarie.")
#if nameresult3: print nameresult3.group(0)
def FindAmericanExtendedDate(text):
    result =  re.compile(r"(January|February|March|April|May|June|July|August|September|October|November|December) [0-9]{1,2}(,)?(st)?(th)? (?=[0-9]{4})[0-9]{4}").search(text)
    if (result == None):
        return ""
    else:
        return result.group(0)

def FindAmericanCondensedDate(text):
    result = re.compile(r"[0-9]{2}\/[1-3][0-9]\/[0-9]{2}").search(text)
    if (result == None):
        return ""
    else:
        return result.group(0)
def FindEuropeanExtendedDate(text):
    result =  re.compile(r"[0-9]{1,2}(,)?(st)?(th)? (January|February|March|April|May|June|July|August|September|October|November|December) (?=[0-9]{4})[0-9]{4}").search(text)
    if (result == None):
        return ""
    else:
        return result.group(0)

# Given an action word (born, died, graduated, etc.) finds the next 20 characters after word 
def FindSearchRange(actions, text):
    out = []
    for action in actions:
        regex = "(?<=" + action + ").{0,40}"
        regex.encode('string-escape')
        out = out + re.findall(regex, text, re.DOTALL)
    return out

# Finds action word in query. 
def FindActionInQuery(query):
    result = re.compile(r"born|died|graduated|elected|die").search(query)
    return result.group(0)

# Takes an action word and generates related words. Ideally I'd use a thesaurus and have this adapt to search queries, but that's too much work
def FindKeyWords(action):
    keyWords = { 'born':['born', 'birth', 'birthday'], 'die':['die', 'Died', 'death', 'passed away', 'born'], 'elected':['elected', 'president', 'election', 'won', 'elect'], 'graduated':['graduated', 'graduate', 'school', 'college', 'university']}
    if action in keyWords:
        return keyWords[action]
    else:
        return [action]

# Often dates are in parentheses 
def FindParentheses(text):
    result = re.findall(r"\(.{40}", text)
    return result
#
#
#
#
#
#
#
#
#