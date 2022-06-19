from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    stdin.readline() #read in blank line
    N = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    sol,S,H = 0,0,{0:1}
    for i in range(N): #O(N)
        S += arr[i]
        if S - 47 in H:
            sol += H[S - 47]
        H[S] = 1 if S not in H else H[S] + 1
    stdout.write(f"{sol}\n")
