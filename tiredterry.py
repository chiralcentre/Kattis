from collections import deque
from sys import stdin,stdout

#sliding window of p seconds
n,p,d = map(int,stdin.readline().split())
pattern = stdin.readline().strip()*2
window,asleep = deque([]),0
for i in range(n-p+1,n+1):
    char = pattern[i]
    if char == "Z":
        asleep += 1
    window.append(char)

tired = 1 if asleep < d else 0
for j in range(n+1,2*n):
    letter = window.popleft()
    if letter == "Z":
        asleep -= 1
    char = pattern[j]
    if char == "Z":
        asleep += 1
    window.append(char)
    if asleep < d:
        tired += 1
stdout.write(str(tired))
    
    
    
