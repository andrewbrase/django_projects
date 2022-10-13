# regular expressions allow us to search for patterns in Python strings

# import re
# # import the regular expressions module

# patterns = ['term1','term2']

# text = 'this is a string to sort through for term1 and NOT the other term'

# for pattern in patterns:

#     print("i'm searching for " + pattern)

#     if re.search(pattern,text):
#         print("found a match in the pattern!")
#     else:
#         print('no match found')

    #  Directory of C:\Users\brasea\Desktop\Workspace\Back_end_web_development\01 Python and Django

# 07/26/2022  01:11 PM    <DIR>          .
# 07/26/2022  01:11 PM    <DIR>          ..
# 07/25/2022  08:11 AM               342 01 NOTES.txt
# 07/25/2022  08:53 PM             8,108 01 OOP_a_refresh.ipynb
# 07/26/2022  10:13 AM             4,248 01 OOP_project.ipynb
# 07/26/2022  12:39 PM             4,810 02 errors_and_exceptions_refresh.ipynb
# 07/26/2022  12:36 PM                25 02 simple.txt
# 07/26/2022  01:03 PM               300 03_regular_expressions.py
#                6 File(s)         17,833 bytes
#                2 Dir(s)  58,214,735,872 bytes free

# C:\Users\brasea\Desktop\Workspace\Back_end_web_development\01 Python and Django>python3.10 03_regular_expressions.py
# i'm searching for term1
# found a match in the pattern!
# i'm searching for term2
# no match found

# C:\Users\brasea\Desktop\Workspace\Back_end_web_development\01 Python and Django>

# match = re.search(pattern,text):
# print(type(match)) --> SRE_Match - more than a boolean or none,
#  this contains info on where the match starts as well as where the match ends


# import re


# text = 'this is a string to sort through for term1 and NOT the other term'

# match =  re.search('term1',text)

# print(match.start())

# starts at index position of 37
# regular expressions also have the ability to split a string in a pattern

# ~~~~~~~~~~~~~

# import re 

# split_term = "@"

# email = "jackjohnson@gmail.com"

# print(re.split(split_term,email))
# --> ['jackjohnson', 'gmail.com']
# can also do 'user@gmail.com'.split('@')

# can use re.findall - to find all of the instances of something
import re 

# print(re.findall('match','test phrase match in middle second time for match'))
# --> ['match', 'match']
# could check length of findall

def mult_re_find(patterns,phrase):
    for pat in patterns:
        print("searching for pattern {}".format(pat))
        # find all ({3},'sdsdsds')
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
# want to find s followed by 0 or more d's
test_paterns = ['[^!.?]+']

mult_re_find(test_paterns,test_phrase)
# 'sdsd..sssddd..sddddsdddd...dsds...dsssss...sddddd'
# * sign means one or more
# --> ['sd', 'sd', 's', 's', 'sddd', 'sdddd', 'sdddd', 'sd', 's', 's', 's', 's', 's', 's', 'sddddd']

# + sign means zero or more d's
# --> ['sd', 'sd', 'sddd', 'sdddd', 'sdddd', 'sd', 'sddddd']

# ? sign 0 or 1 time
# --> ['sd', 'sd', 's', 's', 'sd', 'sd', 'sd', 'sd', 's', 's', 's', 's', 's', 's', 'sd']

# sd{3} three times
# --> ['sddd', 'sddd', 'sddd', 'sddd']

# want to know where s is followed by multiple letters
# s[sd]+ (one or more s's or one or more d's)
# --> ['sdsd', 'sssddd', 'sddddsdddd', 'sds', 'sssss', 'sddddd']

# exclusion 
# This is a string! But it has punctuation. How can we remove it?
# can use 'carrot' symbol ^ to exclude terms
# [^!.?]+
# look for one or more instances of ! . and ? and exclude them
# --> ['This is a string', ' But it has punctuation', ' How can we remove it']

# [a-z]+ instances of lowercase letters
# [A-Z]+ instances of capital letters
# [r'\d+'] - returns numbers 
# [r'\D+'] - returns non digits
# [r'\s+'] - returns whitespace
# [r'\S+'] - non whitespace 
# [r'\w+'] - (letters and numbers) alpha numeric characters 
# [r'\D+'] - (something like hashtag) non alpha numeric

# https://docs.python.org/3/library/re.html