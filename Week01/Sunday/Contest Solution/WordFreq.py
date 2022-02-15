import sys # Подключаем модуль sys для бесконечного ввода(sys.stdin.read())
from collections import Counter # Из модуля collections берем функцию Counter

inp = sys.stdin.read() # бесконечный ввод
# inp = 'the day is sunny the the\nthe sunny is is'

inp = inp.split() # Разделяем пробелами и новыми строками 
# ['the', 'day', 'is', 'sunny', 'the', 'the', 'the', 'sunny', 'is', 'is']

inp = dict(Counter(inp)) # Подсчитываем используя Counter
# {'the': 4, 'day': 1, 'is': 3, 'sunny': 2}

inp = sorted(inp.items(), key=lambda x:x[0]) # Сорт по ключу
# Так как у нас ключом является строка, сортировка будет в алфавитном порядке
# [('day', 1), ('is', 3), ('sunny', 2), ('the', 4)]

inp = Counter(dict(inp)).most_common() # Сорт по значениям
# .most_common() - встроенная функция для Counter - сортирует по самым частовстречающимся
# [('the', 4), ('is', 3), ('sunny', 2), ('day', 1)]

# Остается пройтись по элементам и вывести
# Для этого переводим из [('the', 4), ('is', 3), ('sunny', 2), ('day', 1)] в dict()
# И чтобы вывести и ключи и значения одновременно, используем функцию items() для дикшнари
for key, value in dict(inp).items():
    print(f'{key}: {value}')

# Решение в одну строку:
# print('\n'.join([f'{key}: {value}' for key, value in dict(Counter(dict(sorted(dict(Counter(sys.stdin.read().split())).items(), key=lambda x:x[0]))).most_common()).items()]))
