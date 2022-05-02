from sys import stdin,stdout

n = int(stdin.readline())
cards = sorted(list(map(int,stdin.readline().split()))) #O(n log n)
counter = cards[0] #add smallest card at start, which will always be included in counter
for d in range(n-1,0,-1): #O(n), stop at index d = 1
    if cards[d] > cards[d-1] + 1: #not part of a consecutive sequence
        counter += cards[d]
stdout.write(f'{counter}')
        
