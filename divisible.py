from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    d,n = map(int,stdin.readline().split())
    seq = list(map(int,stdin.readline().split()))
    #compute prefix sums modulo d
    #if two prefix sums have the same remainder, their difference is divisible by d
    #algorithm runs in O(n + d) time
    prefix_sums,counter = [],0
    #O(n)
    for i in range(n):
        counter += seq[i]
        counter %= d
        prefix_sums.append(counter)
    remainders = {}
    for r in prefix_sums:
        remainders[r] = 1 if r not in remainders else remainders[r] + 1
    #O(d)
    subseq = 0
    if 0 in remainders:
        subseq += remainders[0]
    subseq += sum(remainders[k]*(remainders[k]-1)//2 for k in remainders)
    stdout.write(f"{subseq}\n")
        
            
            
    
    
