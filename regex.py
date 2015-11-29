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
#			Generally, a name will not contain more than one dash. Some names may contain more than one apostrophe. (ex. Ku'oko'a)
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
#		Same rules as for first names.
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
def FindName(text):
    return re.compile(r"""
					(											# First name:
					(?:[A-Z']									# starts with capital letter
					([a-z][-|A-Z][a-z]|[a-z]'|[a-z])+[ ])		# followed by capitals or dashes surrounded by lowercase letters OR apostrophes following a lowercase letter OR just lowercase letters
					|											# or
					(?:[A-Z]\.[ ])   							# is just an initial
					)
					(											# Middle name(s): (optional)
					(?:[A-Za-z']								# Same as above, except it can start with uppercase letter
					([a-z][-|A-Z][a-z]|[a-z]'|[a-z])+[ ])		
					|						
					(?:[A-Z]\.[ ])   		
					)
					{0,5}										# Allow for up to five middle names
					(											# Last name:
					(?:[A-Z']									# Same as first name
					([a-z][-|A-Z][a-z]|[a-z]'|[a-z])+)		
					|					
					(?:[A-Z]\.)   		
					)	
                      """, re.X).search(text)
#nameresult1 = name.search("Thomas Edison a name not an Arthur C. Clarcke ")
#if nameresult1: print nameresult1.group(0)
#nameresult2 = name.search("This is a normal sentence without any names.")
#if nameresult2: print nameresult2.group(0)
#nameresult3 = name.search("This is a normal sentence with a really weird name: McAnd're van 'tala D. C. AnneMarie.")
#if nameresult3: print nameresult3.group(0)
def FindAmericanExtendedDate():
    result =  re.findall(r"(January|February|March|April|May|June|July|August|September|October|November|December) [0-9]{1,2}(,)?(st)?(th)? (?=[0-9]{4})[0-9]{4}", text, re.MULTILINE)
    print result

def FindAmericanCondensedDate(text):
    result = re.findall(r"[0-9]{2}\/[1-3][0-9]\/[0-9]{2}", text, re.MULTILINE)
    

# Adapted from StackOverFlow response by Unihedron
# http://stackoverflow.com/questions/24656131/regex-for-existence-of-some-words-whose-order-doesnt-matter
#
# 
# [0-9]{2}\/[1-3][0-9]\/[0-9]{2}
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#