import sys
from collections import Counter

s = sys.stdin.read()
d = dict(Counter(s).most_common())
newdict = dict(sorted(d.items(), key=lambda x: x[0]))
newdict = dict(Counter(newdict).most_common())
print(newdict)

for key, value in newdict.items():
    print(f'{key} - {value}')

# s = '''Hello World!
# My name is Nurtay
# I'm 18 years old
# slfhsd
# fasdafsdjkafasafkdlks dfhsd jlkfsh jd f
# Hello
# World
# 18
# 18 18 18'''