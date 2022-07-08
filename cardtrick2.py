from sys import stdin,stdout
from collections import deque

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    numbers,lst = [i for i in range(1,n+1)],deque([])
    numberOfShifts = n
    for i in range(n-1,-1,-1):
        lst.appendleft(numbers[i])
        for j in range(numberOfShifts):
            lst.appendleft(lst.pop())
        numberOfShifts -= 1
    stdout.write(' '.join(str(card) for card in lst)+'\n')
    
    
