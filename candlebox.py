from math import sqrt
D,R,T = [int(input()) for i in range(3)]

# Rita's age is calculated through sum of arithmetic progression and quadratic formula
# positive square root is taken since Rita's age is positive
age_R = int(((2*D-2)+sqrt((2*D-2)**2-8*(D**2-D-2*(R+T)-18)))/4)
candles_R = sum([i for i in range(4,age_R+1)])
print(R-candles_R)
    
#two liner code
'''
D,R,T = [int(input()) for i in range(3)]
print(R-sum([i for i in range(4,int(((2*D-2)+sqrt((2*D-2)**2-8*(D**2-D-2*(R+T)-18)))/4)+1)]))
'''
