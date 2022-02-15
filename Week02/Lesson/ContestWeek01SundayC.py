import sys
from collections import Counter

d = dict()
inp = sys.stdin.read().lower()
text = ''

for i in range(len(inp)):
    if 'a' <= inp[i] <= 'z':
        text += inp[i]

print('\n'.join([f'{key}: {value}' for key, value in dict(sorted(dict(Counter(text)).items(), key=lambda x:x[0])).items()]))
