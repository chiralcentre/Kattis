requests = {}

for i in range(int(input())):
    firstname,lastname,course = input().split()
    if course not in requests:
        requests[course] = {(firstname,lastname)}
    elif (firstname,lastname) not in requests[course]:
        requests[course].add((firstname,lastname))

for key,value in sorted(requests.items()):
    print(f'{key} {len(value)}')
