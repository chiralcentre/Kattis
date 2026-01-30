from sys import stdin

N = int(stdin.readline())
best,ans = pow(10,9),"INCOMPLETE"
for i in range(N):
    line = stdin.readline().strip()
    W,L = 0,0
    for j in range(len(line)):
        if line[j] == "W":
            W += 1
        else:
            L += 1
        if L == 3:
            W,L = 0,0
        if W == 12 and j < best:
            best,ans = j,str(i + 1)
            break
print(ans)
            
    
