inp = range(15)

print(list(map(lambda x: x**2, inp)))
print()
print(list(filter(lambda x: x % 2 == 1, inp)))
print()
print(list(map(lambda x: x**2, inp)))
# map(function, list1)
# filter(function, list1)

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1], reverse=True)

print(a)

# lambda - мини-функция