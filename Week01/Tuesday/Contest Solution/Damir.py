n, ans = int(input()), []

for i in range(10, 100):
    if str(i)[0] in '01689' and str(i)[1] in '01689': ans.append(i)
    if len(ans) == n:
        print(*ans)
        exit()
print('Glupenky Damir')