for _ in range(int(input())):
    l,m = map(int,input().split())
    l *= 100 #convert length into centimetres for ease of calculations
    banks,crossings = {'left':0,'right':0},{'left':0,'right':0}
    for i in range(m):
        car_length,bank = input().split()
        if int(car_length) <= l: # car can fit on ferry
            if banks[bank] + int(car_length) > l:
                banks[bank] = int(car_length) 
                crossings[bank] += 1
            else:
                banks[bank] += int(car_length)  
    if banks['left'] > 0:
        crossings['left'] += 1
    if banks['right'] > 0:
        crossings['right'] += 1
    print(2*crossings['right']) if crossings['left'] <= crossings['right'] else print(2*crossings['left'] - 1) #start from left bank
