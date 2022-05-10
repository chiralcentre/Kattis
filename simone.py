from sys import stdin,stdout

N,K = map(int,stdin.readline().split())
colours = stdin.readline().split()
frequency = [0 for i in range(K)] #this array acts as a DAT, frequency[i] returns frequency of i+1
for c in colours: #O(N)
    frequency[int(c)-1] += 1
L = min(frequency) #O(K)
lowest = [str(i+1) for i in range(K) if frequency[i] == L] #O(K)
stdout.write(f'{len(lowest)}\n')
stdout.write(' '.join(lowest))
    
