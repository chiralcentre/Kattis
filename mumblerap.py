from sys import stdin,stdout

N,S = int(stdin.readline()),stdin.readline().strip()
ans,p,i = -1,1000000000,0
while i < N:
    if S[i].isdigit():
        p = i
        while i < N and S[i].isdigit():
            i += 1
        num = int(S[p:i])
        ans = max(ans,num)
    i += 1
stdout.write(f"{ans}\n")
