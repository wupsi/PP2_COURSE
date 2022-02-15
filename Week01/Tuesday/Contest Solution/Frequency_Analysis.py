from collections import Counter
import sys

search_range = float(input())
text = ''.join(sys.stdin.read().split())
d, used = {}, []
relative = dict(Counter({'A': 7.9, 'B': 1.4, 'C': 2.7,
            'D': 4.1, 'E': 12.2, 'F': 2.1,
            'G': 1.9, 'H': 5.9, 'I': 6.8, 
            'J': 0.2, 'K': 0.8, 'L': 3.9, 
            'M': 2.3, 'N': 6.5, 'O': 7.2,
            'P': 1.8, 'Q': 0.1, 'R': 5.8,
            'S': 6.1, 'T': 8.8, 'U': 2.7,
            'V': 1.0, 'W': 2.3, 'X': 0.2,
            'Y': 1.9, 'Z': 1.0}).most_common())

letters = dict(Counter(text).most_common())
for i in range(26): 
    if chr(i + 65) not in letters.keys(): letters[chr(i + 65)] = 0.0

for key, value in letters.items():
    letters[key] = round(value / len(text) * 100, 2)

for i in range(26):
    # print(f'{list(letters.keys())[i]} - {list(letters.values())[i]}', 
    #       f'| {list(relative.keys())[i]} - {list(relative.values())[i]}')
    lett_items = (list(letters.keys())[i], list(letters.values())[i])
    rel_items = (list(relative.keys())[i], list(relative.values())[i])

    for j in range(26):
        ex = list(relative.values())[j]
        # print(lett_items[1] - search_range, ex, lett_items[1] + search_range)
        if lett_items[1] - search_range <= ex <= lett_items[1] + search_range:
            if lett_items[0] not in d.keys() and lett_items[1] != 0: d[lett_items[0]] = []
            if lett_items[1] != 0: d[lett_items[0]].append(list(relative.keys())[j])

elem = list(d.items())

for a in range(len(elem[0][1])):
    if elem[0][1][a] not in used: used.append(elem[0][1][a])
    for b in range(len(elem[1][1])):
        if elem[1][1][b] not in used: used.append(elem[1][1][b])
        for c in range(len(elem[2][1])):
            if elem[2][1][c] not in used: used.append(elem[2][1][c])
            for d in range(len(elem[3][1])):
                if elem[3][1][d] not in used: used.append(elem[3][1][d])
                for e in range(len(elem[4][1])):
                    if elem[4][1][e] not in used: used.append(elem[4][1][e])
                    for f in range(len(elem[5][1])):
                        if elem[5][1][f] not in used: used.append(elem[5][1][f])
                        for g in range(len(elem[6][1])):
                            if elem[6][1][g] not in used: used.append(elem[6][1][g])
                            for h in range(len(elem[7][1])):
                                if elem[7][1][h] not in used: used.append(elem[7][1][h])
                                for i in range(len(elem[8][1])):
                                    if elem[8][1][i] not in used: used.append(elem[8][1][i])
                                    for j in range(len(elem[9][1])):
                                        if elem[9][1][j] not in used: used.append(elem[9][1][j])
                                        for k in range(len(elem[10][1])):
                                            if elem[10][1][k] not in used: used.append(elem[10][1][k])
                                            for l in range(len(elem[11][1])):
                                                if elem[11][1][l] not in used: used.append(elem[11][1][l])
                                                for m in range(len(elem[12][1])):
                                                    if elem[12][1][m] not in used: used.append(elem[12][1][m])
                                                    for n in range(len(elem[13][1])):
                                                        if elem[13][1][n] not in used: used.append(elem[13][1][n])
                                                        for o in range(len(elem[14][1])):
                                                            if elem[14][1][o] not in used: used.append(elem[14][1][o])
                                                            for p in range(len(elem[15][1])):
                                                                if elem[15][1][p] not in used: used.append(elem[15][1][p])
                                                                for q in range(len(elem[16][1])):
                                                                    if elem[16][1][q] not in used: used.append(elem[16][1][q])
                                                                    for r in range(len(elem[17][1])):
                                                                        if elem[17][1][r] not in used: used.append(elem[17][1][r])
                                                                        for s in range(len(elem[18][1])):
                                                                            if elem[18][1][s] not in used: used.append(elem[18][1][s])
                                                                            for t in range(len(elem[19][1])):
                                                                                if elem[19][1][t] not in used: used.append(elem[19][1][t])
    print(used)

# B - 'E'
# R - 'T'
# G - 'A'
# N - 'O'
# I - 'I'
# A - 'N'
# U - 'S'
# K - 'H'
# O - 'R'
# J - 'D'
# X - 'L'
# L - 'C'
# F - 'U'
# M - 'M'
# E - 'W'
# S - 'F'
# Z - 'G'
# C - 'Y'
# T - 'P'
# W - 'B'
# P - 'V'
# V - 'Z'
# Q - 'K'