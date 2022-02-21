import re

text = '''1.
Оплачено: Steam
nickname: wups1k
Сумма - 100,00 тг
№ квитанции 1234325729350934
Дата платежа 04.12.2021 04:30:04
ФИО плательщика Жолдаскалиев Н. Ж.
Оплачено с Kaspi Gold

2.
Оплачено: Steam
nickname: wups1k
Сумма - 1 100,00 тг
№ квитанции 1234465369350934
Дата платежа 04.12.2021 04:28:40
ФИО плательщика Жолдаскалиев Н. Ж.
Оплачено с Halyk Bank

3.
Оплачено: Steam
nickname: ammoinnyaa
Сумма - 1 000,00 тг
№ квитанции 20474176398346
Дата платежа 16.02.2022 11:21:24
ФИО плательщика Оразгали А. Е.
Оплачено с Forte Bank
'''

nicknames = re.findall(r'nickname: (.+)', text)
banks = re.findall(r'Оплачено с (.+)', text)
date = re.findall(r'(\d{2}\.\d{2}\.\d{4})', text)
time = re.findall(r' (\d{2}:\d{2}:\d{2})', text)
fail = re.findall(r'Оплаачено с (.+)', text)
sums = re.findall(r'Сумма - (.+),', text)
summm = 0
words = re.split(r'\s', text)

print('nicknames:', ', '.join([i for i in nicknames]))
print('banks:', ', '.join([i for i in banks]))
print('dates:', ', '.join([i for i in date]))
print('times:', ', '.join([i for i in time]))
if fail: print('pattern exists!')
else: print("pattern doesn't exists")

for i in sums:
    y = int(''.join(re.split(r'\s', i)))
    summm += y

print('Sum:', summm)
print(words)

# samp = 'hello world my name is Nurtay'
# x = re.search(r'(.+) (.+) (.+)', samp)
# print(f'Start pos: {x.start()}, end pos: {x.end()}')
# print('Span:', x.span(), x.span()[0], x.span()[1])
# print(f'x[0]: {x[0]}')
# print(f'x[1]: {x[1]}')
# print(f'x[2]: {x[2]}')
# print(f'x[3]: {x[3]}')

# re.findall()
# re.split()
# re.sub()

# sums = ['100', '1 100', '1 000']

# i = ['100'] -> '100' -> 100
# i = ['1', '100'] -> '1100' -> 1100
# i = ['1', '000'] -> '1000' -> 1000
