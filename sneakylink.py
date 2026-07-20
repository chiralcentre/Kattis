from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n,c = map(int,stdin.readline().split())
    # take all fragments with positive values
    neg,values = [],list(map(int,stdin.readline().split()))
    ans = 0
    for v in values:
        if v >= 0:
            ans += v
        else:
            neg.append(v)
    neg.sort()
    for i in range(len(neg)):
        v = -neg[i]
        d = v - (i + 1) * c
        if d > 0:
            ans += d
        else:
            break
    stdout.write(f"{ans}\n")
            
        
    
