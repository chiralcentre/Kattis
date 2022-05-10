from sys import stdin,stdout

N = int(stdin.readline())
cards = sorted(map(int,stdin.readline().split())) #O(N log N)
frequency = {} #sum of values in hash table = minimum number of turns
for c in cards:
    frequency[c] = 1 if c not in frequency else frequency[c] + 1
    if c - 1 in frequency: #part of a consecutive sequence
        frequency[c-1] = max(0,frequency[c-1]-1) #only subtract 1 if frequency[c-1] > 0
stdout.write(f'{sum(frequency.values())}')
    
