from sys import stdin,stdout

N = int(stdin.readline())
p1 = list(map(int,stdin.readline().split()))
p2 = [0 for i in range(N)]
second = list(map(int,stdin.readline().split()))
for i in range(N): #O(N)
    p2[p1[i]-1] = second[i]
seen = [False for _ in range(N)]; swaps = N
for i in range(N): #O(N)
    if not seen[i]:
        swaps -= 1
        j = i
        while not seen[j]:
            seen[j] = True
            j = p2[j] - 1
stdout.write("Impossible") if swaps%2 else stdout.write("Possible")
    
      
