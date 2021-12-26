average,shares = 0,0

while True:
    event = input().split()
    if event[0] == 'die':
        profit = max(int(event[1])-average,0)
        print(shares*(int(event[1])-(profit*0.3)))
        break
    elif event[0] == 'buy':
        new = shares + int(event[1])
        average = (average*shares + int(event[1])*int(event[2]))/new
        shares = new
    elif event[0] == 'sell':
        shares -= int(event[1])
    elif event[0] == 'split':
        shares *= int(event[1])
        average /= int(event[1])
    elif event[0] == 'merge':
        shares //= int(event[1])
        average *=  int(event[1])
    
        
