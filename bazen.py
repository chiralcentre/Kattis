def bazen(pos): #calculations are derived using shoelace formula
    a,b = pos[0],pos[1]
    if a == 0 and 0 <= b <=250: #height
        if 125 < b <= 250:
            c,d = 31250/b,0
        else:
            c = (31250-125*a)/(250-b-a)
            d = 250 - c
    elif 0 < a <= 250 and b == 0: #base
        if 125 < a <= 250:
            c,d = 0,31250/a
        else:
            c = (31250-125*b-250*a)/(250-b-a)
            d = 250 - c
    elif 0 < a < 250 and 0 < b < 250:
        if 125 < a < 250:
            c,d = 0,(125*a-125*b)/a
        else:
            c,d = (125*b-125*a)/b,0
    return [str("{:.2f}".format(c)),str("{:.2f}".format(d))]      

endpoint = tuple(map(int,input().split()))
print(' '.join(bazen(endpoint)))
