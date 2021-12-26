def distance_squared(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def midpoint(a,b):
    return((a[0]+b[0])/2,(a[1]+b[1])/2)

def vertex(a,b,c):
    lst = [distance_squared(a,b),distance_squared(a,c),distance_squared(b,c)]
    if lst[0] == lst[1]:
        return a
    elif lst[0] == lst[2]:
        return b
    elif lst[1] == lst[2]:
        return c

def completingthesquare(a,b,c):
    lst = [a,b,c]
    n = vertex(a,b,c)
    for point in lst:
        if point == n:
            lst.remove(n)
    midpt = midpoint(lst[0],lst[1])
    return f'{int(2*midpt[0]-n[0])} {int(2*midpt[1]-n[1])}'

n1 = tuple(map(int,input().split()))
n2 = tuple(map(int,input().split()))
n3 = tuple(map(int,input().split()))
print(completingthesquare(n1,n2,n3))      
