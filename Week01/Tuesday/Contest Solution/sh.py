from collections import Counter
import sys

inp = dict(Counter(sys.stdin.read()))
del inp['\n']
del inp[' ']

for i in range(26):
    if chr(i + 65) not in inp.keys(): inp[chr(i + 65)] = 0

inp = sorted(inp.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)

for i in range(len(inp)):
    print(f'{inp[i][0]} - {inp[i][1]}, {round(inp[i][1] / 253 * 100, 3)}%')
