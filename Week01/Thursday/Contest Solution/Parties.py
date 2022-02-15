d = {}
for i in range(int(input())): d[input()] = 0
for i in range(int(input())): d[input()] += 1
for key, value in d.items():  
    if value / sum(d.values()) * 100 > 7: print(key)