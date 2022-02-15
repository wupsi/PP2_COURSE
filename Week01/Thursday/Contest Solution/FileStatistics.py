ans, letters, symbols = [], 0, 0
for i in range(int(input())):
    for j in input().split():
        ans.append(j)
        for k in j:
            if k.isalpha(): letters += 1
            else: symbols += 1

print(f'File contains:\n{letters} letters\n{len(ans)} words\n{symbols} symbols')