import sys
from collections import Counter

d = dict()
inp = sys.stdin.read().split()
for key, value in dict(Counter(dict(sorted(dict(Counter(inp)).items(), key=lambda x:x[0]))).most_common()).items():
    print(f'{key}: {value}')


# everything: 6
# will: 4
# be: 3
# fine: 1
