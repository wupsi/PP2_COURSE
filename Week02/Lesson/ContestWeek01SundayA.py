d = dict()
for i in range(int(input())):
    inp = input().split() # ['n_zholdaskaliev', 'add', 'math_foundation', 'web_dev']
    email, req, disciplines = inp[0], inp[1], inp[2:] 
    # email = 'n_zholdaskaliev', req = 'add', disciplines = ['math_foundation', 'web_dev']
    if email not in d.keys(): d[email] = list()
    if req == 'add': 
        for disc in disciplines: d[email].append(disc)
    elif req == 'drop':
        for disc in disciplines: d[email].remove(disc)

# for key, value in sorted(d.items()):
#     print(f'{key}:', *value)
    
# email: 'n_zholdaskaliev'
# req: 'add' 
# disciplines: ['math_foundation', 'web_dev']

# d = {'n_zholdaskaliev': ['math_foundation', 'web_dev']}
# d['n_zholdaskaliev'] -> []
# d[email] -> []
# {'n_zholdaskaliev': ['math_foundation', 'web_dev']}
# d['n_zholdaskaliev'] -> ['math_foundation', 'web_dev']

# print(d)
# print('dict keys:', list(d.keys()))
# print('dict values:', list(d.values()))
# print('dict items:', list(d.items()))

# ('green', ['deagle', 'smoke', 'AK-47'])

# for i, j in list(d.items()):
#     print(i, *j)