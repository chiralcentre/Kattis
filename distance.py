def distance(lst):
    lst = sorted(lst)
    counter,ans = 0,0
    for i in range(1,len(lst)):
        counter += i*(lst[i]-lst[i-1])
        ans += counter
    return ans
    
x,y = [],[]

for i in range(int(input())):
    a,b = tuple(map(int,input().split()))
    x.append(a)
    y.append(b)
    
print(distance(x) + distance(y))
            
