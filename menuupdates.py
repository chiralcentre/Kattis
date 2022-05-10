from sys import stdin,stdout
from heapq import heappush,heappop

d,U = map(int,stdin.readline().split())
removed = []; counter = 1
for i in range(U):
    command = stdin.readline().split()
    if command[0] == 'a':
        if not removed or removed[0][0] > i:
            stdout.write(f'{counter}\n')
            counter += 1
        else:
            temp = []; lowest = 1000000000 #use 1 billion as an arbitrarily large number
            while removed and removed[0][0] <= i:
                a,b = heappop(removed)
                if b < lowest:
                    lowest = b
                temp.append((a,b))
            while temp: #add back
                a,b = temp.pop()
                if b != lowest:
                    heappush(removed,(a,b))   
            stdout.write(f'{lowest}\n')
    elif command[0] == 'r':
        b = int(command[1])
        heappush(removed,(i+d,b)) #left attribute is day the number is ready, and right attribute is number
