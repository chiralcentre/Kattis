from sys import stdin,stdout
from math import ceil

program = stdin.readline().strip()
params,smallest = 3,0
for char in program:
    if char.isupper():
        smallest += ceil((params + 1)/4) * 4 - params - 1
        params = 0
    else:
        params += 1
stdout.write(f"{smallest}") 
