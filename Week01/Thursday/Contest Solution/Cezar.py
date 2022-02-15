ans = []
for i in range(int(input())):
    inp = list(input())
    for j in range(i + 1):
        for k in range(len(inp)):
            inp[k] = chr(ord(inp[k]) + 1)
            if inp[k] == '[': inp[k] = 'A'
    ans.append(inp)

print('\n'.join([''.join(i) for i in ans]))