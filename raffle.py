#Let x be the numebr of times to add own name to box
#Let X be the random variable which is the number of times own name is drawn
#X follows a hypergeometric distribution
#P(X = 1) will increase as long as x <= n/(p-1)
n,p = map(int,input().split())
x = n//(p-1)
probability = x*p/(n+1)
for i in range(2,x+1):
    probability *= (n-p+i)/(n+i)
print(probability)
    
