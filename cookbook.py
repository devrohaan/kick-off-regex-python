#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:11:33 2016

@author: Rohan
"""

'''
a technique to extract and manipulate specific string patterns from a larger text.

It is widely used in natural language processing, mostly for preprocessing the text. 
web applications that require validating string input (like email address). 
pretty much most data science projects that involve text mining from large data sets.


. ^ $ * + ? { [ ]  | ( )  These are meta characters with special meaning


\ ###very important  ...escapes a special character.

s one [small s] whitespace

S one non whitespace # anything other than a space

+ one or more

*   0 or more 

d any digit [0 to 9]

D any non digit [^0-9]
. 
matches any single character except newline 'n'

w matches a single charater out of [A-Za-z0-9_] = word characters,  w is all alphanumeric characters

W matches a non world character [^A-Za-z0-9_] ^ comes inside the group

\b            Word boundary
\B            will match any non-boundary

\n            Newline
\t            Tab
^           match the start of the string
$           match the of the string end
?           matches exactly 0 or 1  colou?r # 0 or exactly 1 occurence of u
[ab-d]	     One character of: a, b, c, d


'''
import re


text = """101 COM    Computers
205 MAT   Mathematics
189 ENG   English"""


# why do we compile regex pattern?
# -> 
"""
Compile process parses the regular expression and builds an in-memory representation of the regex string. 

The overhead to compile is significant compared to a match. 

If you're using a pattern repeatedly it will gain some performance to cache the compiled pattern.

"""

pattern = r"\s+"

regex = re.compile(pattern)

listobj = regex.split(text)  # spilt when you find one or nore whitespaces

print(listobj) #['101', 'COM', 'Computers', '205', 'MAT', 'Mathematics', '189', 'ENG', 'English']

alternate = re.split('\s+', text) # not a good practice as mentioned reason


#####


pattern = r"\d+"

regex = re.compile(pattern)

listobj = regex.findall(text)  # ['101', '205', '189']

####


'''
findall vs search vs match

findall - returns the matched portions of the text as a list
            scanned left-to-right
            non-overlapping matches of pattern 

search - returns a match object contains [starting and ending positions of the first occurrence of the pattern]
         returns None (if the pattern not present)
         This method stops after the first match
         
match - returns a match object. But the difference is, 
        it requires the pattern to be present at the beginning of the text itself.
        In between is not matched
        basically string must start with the pattern
        else None
'''


# re.findall(pattern, text, flags=re.IGNORECASE)

'''
very very powerful hack
'''
re.findall('[a-z]+', text, flags=re.IGNORECASE) # ['COM', 'Computers', 'MAT', 'Mathematics', 'ENG', 'English']

listobj = regex.findall(text)  # ['101', '205', '189']

matchobj =  regex.search(text)


# stops after the first match ie 101

print(matchobj.start()) # 0
print(matchobj.end())   # 3
print(matchobj.span())  # (0,3)
print(matchobj.group()) # 101
print(matchobj.group(0)) # 101



# match will retrun null as pattern is 
# tect must initiate with "Wisdomic Panda" and out text starts with 101

pattern = r"wisdomic\s*panda"

regex = re.compile(pattern)

matchobj = regex.match(text) # None

# very important sub

pattern = "\d+"

regex = re.compile(pattern)

string = regex.sub('COURSE_CODE', text) # returns string

print(string)

"""
re.sub('\d+', 'COURSE_CODE', text)

COURSE_CODE COM    Computers
COURSE_CODE MAT   Mathematics
COURSE_CODE ENG   English
"""


# group

'''
[all possible characters]

eg. 
text = 'W!@isdmi&|C P@:an,@da'

list = re.split('[!@,:\s\'|&]+',text) 

''.join(list) # 'WisdmiCPanda'

'''

listobj = re.findall('[A-Z]{3}', text) # ['COM', 'MAT', 'ENG']

listobj = re.findall('[A-Z]{2}', text) # ['CO', 'MA', 'EN']

listobj = re.findall('[A-Za-z]{2}', text) # ['CO', 'Co', 'mp', 'ut', 'er', 'MA', 'Ma', 'th', 'em', 'at', 'ic', 'EN', 'En', 'gl', 'is']

listobj = re.findall('[A-Z]{4}', text) # []

listobj = re.findall('[A-Z]{1,}', text) # ['COM', 'C', 'MAT', 'M', 'ENG', 'E']  will have at least 1 or more characters.


course_pattern = '([0-9]+)\s*([A-Z]{3})\s*([A-Za-z]{4,})'
'''
([0-9]+)
([A-Z]{3})
([A-Za-z]{4,})

'''

text1 = '01, Jan 2015'

pattern = '\d{4}'

regex = re.compile(pattern)

regex.findall(text1) # ['2015']


re.findall('\d{2,4}',text1) # ['01', '2015']

re.findall('J?an',text1) # 'Jan']  0 or exactly 1 occurence of J'


# word boundry

'''
\b is commonly used to detect and match the beginning or end of a word.

\bpanda will match the panda  in ‘pandarohan’ and not in rohanpanda.
In order to match the panda in rohanpanda, you should use panda\b
'''

re.findall(r'\bpanda', 'wisdomic panda not wisdomic pandarohan') # ['panda', 'panda']

re.findall(r'\bpanda\b', 'wisdomic panda not wisdomic pandarohan') #['panda'] gets the exact word panda as we have boundries on both ends.

"""
Find Email Address: if you could write this pattern you are good to go.
"""


string  = 'My name is CR7, and wisdomic@panda.com is my email. robagwe@gmail.com'

pattern = r"\w+@[a-z]+\.[a-z]+"

regex = re.compile(pattern)

listobj = regex.findall(string) # ['wisdomic@panda.com', 'robagwe@gmail.com']

# regex for daily usage...

tmp = re.sub(r'\$\w*','',string) # Remove tickers
tmp = re.sub(r'https?:\/\/.*\/\w*','',string) # Remove hyperlinks
tmp = re.sub(r'['+string.punctuation+']+', ' ',string) # Remove puncutations like 's

