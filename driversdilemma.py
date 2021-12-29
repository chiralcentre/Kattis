C,X,M = map(float,input().split())
speed = 0
for i in range(6):
    s,FE = map(float,input().split())
    GPH = s/FE + X #Gallon per hour lost
    hours = M/s
    if GPH*hours < C/2:
        if s > speed:
            speed = s

print(f'YES {int(speed)}') if speed > 0 else print('NO')

    
