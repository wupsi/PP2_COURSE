import sys # Подключаем модуль sys для бесконечного ввода(sys.stdin.read())

inp = sys.stdin.read().lower() # бесконечный ввод, сразу перевел буквы в строчные функцией .lower() 
# 'machine code was the language of
# early programs, written in the
# instruction set of the particular
# machine, often in binary notation.'

d = dict()
# Подсчет букв из строки inp
for i in inp:
    if 'a' <= i <= 'z': 
        if i not in d.keys(): d[i] = 0
        d[i] += 1

d = sorted(d.items(), key=lambda x:x[0]) # Сорт ключей в алфавитном порядке

for key, value in dict(d).items():
    print(f'{key}: {value}') # Вывод
