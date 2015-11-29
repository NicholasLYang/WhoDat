import regex, utils

actions = ['Died']
text = '''
Died
8 December 1980 (aged 40)

'''
searchRange = regex.FindSearchRange(actions, text)
dates = regex.FindEuropeanExtendedDate(searchRange[0])
print dates

