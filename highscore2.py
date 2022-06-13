from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    *tokens,d = map(int,stdin.readline().split())
    a,b,c = sorted(tokens)
    # a <= b <= c
    # for small values of a,b,c (max(a,b,c) = c <= 6) and d <= 3, brute force will suffice
    # otherwise, simply add d to c
    # the upper bounds are derived via trial and error
    # 6 is tightest upper bound for a and 3 is tightest upper bound for d
    ans = a**2 + b**2 + c**2 + 7*a
    if a <= 6 and d <= 3:
        for i in range(d+1):
            for j in range(d-i+1):
                k = d - i - j
                ans = max(ans,(a+i)**2+(b+j)**2+(c+k)**2+7*min(a+i,b+j,c+k))
    else:
        ans = a**2 + b**2 + (c+d)**2 + 7*a
    stdout.write(f"{ans}\n")
    
    
