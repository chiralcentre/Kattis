t,d,speed = 0,0,0
for _ in range(int(input())):
    t2,d2 = map(int,input().split())
    if t2-t > 0 and (d2-d)//(t2-t) > speed:
        speed = (d2-d)//(t2-t)
    t,d = t2,d2
print(speed)

