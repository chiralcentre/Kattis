def construction(bricks,h,w,n):
    layer_length = 0
    for i in range(n):
        layer_length += bricks[i]
        if layer_length == w:
            h -= 1
            layer_length = 0
            if h == 0:
                return('YES')
        elif layer_length > w:
            return('NO')

h,w,n = map(int,input().split())
bricks = list(map(int,input().split()))
print(construction(bricks,h,w,n))
