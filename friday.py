from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    D,M = map(int,stdin.readline().split())
    months = list(map(int,stdin.readline().split()))
    # the first friday occurs 5 days after start of year
    curr,m,d,ans = 6,0,6,0
    while curr < D:
        temp = d
        while m < M and temp > months[m]:
            temp -= months[m]
            m += 1
        d = temp
        if d == 13:
            ans += 1
        curr += 7
        d += 7
    stdout.write(f"{ans}\n")   
    
        
