from math import ceil
#Let number of days after which low energy lamp is cheaper than incandescent bulb be d.
#Cost of electricity for incandescent bulb = (60*d*h*P)/100000 + ceil(d*h/1000)*5
#Cost of electricity for low energy lamp = (11*d*h*P)/100000 + 60, since number of hours will not exceed 8000
#After rearranging the inequality, we obtain 49*h*P/100000 > (60 - (ceil(d*h/1000))*5)/d
h,P = map(int,input().split())
d = 1 #d != 0
while 49*h*P/100000 <= (60 - (ceil(d*h/1000))*5)/d:
    d += 1
print(d)
