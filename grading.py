a,b,c,d,e = map(int,input().split())
n = int(input())

if n < e:
    print('F')
elif e <= n < d:
    print('E')
elif d <= n < c:
    print('D')
elif c <= n < b:
    print('C')
elif b <= n < a:
    print('B')
else:
    print('A')
