from sys import stdin,stdout

def isOrdered(s,a):
    for i in range(a):
        for j in range(i + 1, a):
            if s[i][0] > s[j][1]:
                return False
    return True

n = int(stdin.readline())
d = [int(stdin.readline()) for _ in range(n)]
ans,INF = [],pow(10,9)
for a in range(2,n + 1):
    if not n % a:
        k = n // a
        s = [[-1,INF] for _ in range(a)]
        for i in range(n):
            p = i // k
            s[p][0] = max(d[i],s[p][0])
            s[p][1] = min(d[i],s[p][1])
        if isOrdered(s,a):
            ans.append(str(a))
stdout.write("\n".join(diff for diff in ans)) if ans else stdout.write("-1\n")
        
