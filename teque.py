from sys import stdin,stdout
from collections import deque
# use two deques to simulate a teque; d1 = front deque, d2 = back deque
d1,d2 = deque([]),deque([])
for linenum,line in enumerate(stdin):
    if linenum > 0: #skip first line
        command,value = line.split()
        if command == 'push_front':
            d1.appendleft(value)
        elif command == 'push_back':
            d2.append(value)
        elif command == 'push_middle':
            d1.append(value) if len(d2) >= len(d1) else d2.appendleft(value)
        else: # get command
            index = int(value)
            if index >= len(d1):
                index %= len(d1)
                stdout.write(d2[index]+'\n')
            else:
                stdout.write(d1[index]+'\n')
    #rebalance deques if necessary such that abs(len(d1) - len(d2)) <= 1
    #rebalance deques if d1 is empty and d2 is occupied
    if len(d1) - len(d2) > 1:
        d2.appendleft(d1.pop())
    elif len(d2) > len(d1):
        d1.append(d2.popleft())

