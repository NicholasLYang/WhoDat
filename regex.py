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
#
#
#
#
#