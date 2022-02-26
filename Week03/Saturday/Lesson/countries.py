# Countries
# —————————————————
# Вам даны 195 стран, их население, площадь земельного участка и плотность населения - 
# количество человек на квадратный метр. Выведите все страны, названия которых оканчиваются 
# на 'stan', затем страны с населением более 5 миллионов и плотностью населения более 50. 
# —————————————————
import re

with open('countries.txt', 'r') as txt:
    txt = txt.read()
    print(txt)
    print("Countries whose names end with 'stan':")
    print(', '.join(re.findall(r'\d+  ([^0-9]+stan)  ', txt)))
    print('Countries with a population of more than 5 million and a population density of more than 50:')
    coun = re.findall(r'\d+  ([^0-9]+)  ([5-9]|\d{2,}|\d+,\d+),\d{3},\d{3}  .+  ([5-9]\d$|[0-9,]{3,})', txt)
    for i in coun: print(i[0])