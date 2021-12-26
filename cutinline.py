queue = [input().strip() for i in range(int(input()))]

for j in range(int(input())):
    event = input().split()
    if event[0] == 'cut':
        for k in range(len(queue)):
            if queue[k] == event[2]:
                queue = queue[:k] + [event[1]] + queue[k:]
                break
    elif event[0] == 'leave':
        queue.remove(event[1])

for person in queue:
    print(person)
