from sys import stdin,stdout
from collections import deque

for _ in range(int(stdin.readline())):
    program = stdin.readline().strip()
    n = int(stdin.readline())
    lst = deque(stdin.readline().strip().lstrip('[').rstrip(']').split(','))
    error,reverse = False, False
    for command in program:
        if command == 'R':
            reverse = False if reverse else True
        else:
            if n != 0:
                lst.pop() if reverse else lst.popleft() #O(1) time complexity
                n -= 1
            else:
                error = True
                break
    if error:
        stdout.write('error\n')
    else:
        stdout.write('[')
        stdout.write(','.join(lst[i] for i in range(n-1,-1,-1))) if reverse else stdout.write(','.join(lst)) 
        stdout.write(']\n')
    
