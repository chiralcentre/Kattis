from sys import stdin,stdout
from collections import deque
from heapq import heappop, heappush

while True:
    try:
        n = int(stdin.readline())
    except:
        break
    stack,queue,PQ,impossible = [],deque([]),[],False
    data_structures = {'stack','queue','priority queue'}
    for _ in range(n):
        command,element = map(int,stdin.readline().split())
        if command == 1:
            stack.append(element)
            queue.append(element)
            heappush(PQ,-element) #since PQ in python is min heap by default
        else:
            if not stack or not queue or not PQ: # check if empty
                impossible = True
            else:
                a,b,c = stack.pop(),queue.popleft(),-heappop(PQ)
                if a != element:
                    data_structures.discard('stack')
                if b != element:
                    data_structures.discard('queue')
                if c != element:
                    data_structures.discard('priority queue')
    if impossible or len(data_structures) == 0:
        stdout.write("impossible\n")
    elif len(data_structures) == 1:
        stdout.write(f'{list(data_structures)[0]}\n')
    elif len(data_structures) > 1:
        stdout.write(f'not sure\n')
    
