row, y = [1], [0]
for i in range(int(input())):
    print(row)
    row = [left + right for left, right in zip(row + y, y + row)]
