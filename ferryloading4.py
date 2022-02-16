for _ in range(int(input())):
    l,m = map(int,input().split())
    l *= 100 #convert length into centimetres for ease of calculations
    left,right,lc,rc = 0,0,0,0
    for i in range(m):
        car_length,bank = input().split()
        if int(car_length) <= l: # car can fit on ferry
            if bank == 'left':
                if left + int(car_length) > l:
                    left = int(car_length) 
                    lc += 1
                else:
                    left += int(car_length)
            else:
                if right + int(car_length) > l:
                    right = int(car_length)
                    rc += 1
                else:
                    right += int(car_length)
    if left > 0:
        lc += 1
    if right > 0:
        rc += 1
    print(2*rc) if lc <= rc else print(2*lc - 1) #start from left bank
