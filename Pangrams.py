import re
text = set(re.sub("[^a-zA-Z]+","",str(input().split()).lower()))
if(len(text) == 26):
    print('pangram')
else:
    print('not pangram')
