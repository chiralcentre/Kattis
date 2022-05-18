from sys import stdin,stdout

#find length of longest contiguous segment of unique snowflakes
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    #occurrences[a] stores the latest occurrence index of a in snowflakes list
    occurrences = {}; s,longest = 0,0
    for i in range(n): #O(n)
        a = int(stdin.readline())
        if a in occurrences:
            s = max(occurrences[a]+1,s) #s stores the index of starting element of contiguous sequences
        longest = max(longest,i-s+1) #i-s+1 is length of contiguous sequence
        occurrences[a] = i
    stdout.write(f'{longest}\n')
        
       
