import json

with open('vk.json', 'r', encoding='utf-8') as txt:
    data = txt.read()

data = json.loads(data)
cnt = 0
summ = 0
print('Кол-во подписчиков:', data['response']['count'], 'человек')

for member in data['response']['items']:
    cnt += 1
    print(f"{cnt}. {member['first_name']} {member['last_name']}, ID: {member['id']}")
    summ += member['id']

print('Сумма айдишек', summ)

# json.loads()

# str -> dict
# str -> list
# '614079840' -> 614079840
# 'true'/'false' -> True/False
