requests = dict()

for i in range(int(input())):
    inp = input().split()
    email, command = inp[0], inp[1]

    if email not in requests.keys(): 
        requests[email] = []

    for j in range(2, len(inp)): 
        if command == 'add': 
            requests[email].append(inp[j])

        elif command == 'drop': 
            requests[email].remove(inp[j])

for key, value in sorted(requests.items()):
    print(str(key) + ':', *value)