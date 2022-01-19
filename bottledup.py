def bottledup(s,v1,v2):
    upper_bound = s//v1
    for i in range(upper_bound,-1,-1):
        if not (s - v1*i)%v2:
            return f"{i} {(s-v1*i)//v2}"
    return "Impossible" 

s,v1,v2 = map(int,input().split())
print(bottledup(s,v1,v2))
