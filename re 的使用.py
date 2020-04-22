import re
print( re.match("hel","hello,world").span() ) #在起始位置匹配
print (re.match("world","hello world"))
print( re.search("hello","hello world").span())