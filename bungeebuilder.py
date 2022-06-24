from sys import stdin,stdout

N = int(stdin.readline())
mountains = list(map(int,stdin.readline().split()))
pairs = [] #contains pairs of indices of mountains for bridge formation

#bridges can only be formed between two mountains with shorter mountains in between
index = 0
for i in range(1,N): #O(N)
    if mountains[i] >= mountains[index]:
        pairs.append((index,i))
        index = i
        
index = N - 1
for i in range(N-2,-1,-1): #O(N)
    if mountains[i] >= mountains[index]:
        pairs.append((i,index))
        index = i

highest = 0
for l,r in pairs: #O(N)
    for j in range(l+1,r):
        if min(mountains[l],mountains[r]) - mountains[j] > highest:
            highest = min(mountains[l],mountains[r]) - mountains[j]
stdout.write(str(highest))
            
    

            
    
        
        
