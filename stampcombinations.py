from sys import stdin,stdout

def solve(q,total):
    if q == 0 or q == total:
        return "Yes"
    if q > total:
        return "No"
    for i in range(m,-1,-1):
        if suffixSums[i] == q:
            return "Yes"
        if suffixSums[i] < q:
            r = q - suffixSums[i]
            if r in prefixSums and prefixSums[r] <= i:
                return "Yes"  
        else:
            return "No"
    return "No"

m,n = map(int,stdin.readline().split())
stamps = list(map(int,stdin.readline().split()))
counter,prefixSums = 0,{}
for i in range(m): #O(m)
    counter += stamps[i]
    prefixSums[counter] = i
total = counter
counter,suffixSums = 0,[0 for _ in range(m+1)]
for i in range(m - 1,-1,-1): #O(m)
    counter += stamps[i]
    suffixSums[i] = counter
#take note that suffixSum arrays is already in sorted order, with length m + 1.
#suffixSum is sorted in decreasing order
#for every query, check every suffix sum s <= q and check if q - s is a prefix sum that starts before the suffix sum
#prefixSums are stored in a hashtable, so check can be done in O(1)
#total time complexity is O(nm)
for i in range(n):
    stdout.write(f"{solve(int(stdin.readline()),total)}\n")
    
            
            
    
