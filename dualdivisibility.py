from sys import stdin,stdout

#Let c be a divisor of a which has b as a divisor
#a = cx, c = by for some positive integers x,y
#y <= 9 by the following argument:
#If y >= 10, a = cx >= c >= 10b, but then a will not have more digits than b, which is a contradiction.
#try out all values of y
a,b = map(int,stdin.readline().split())
counter = 0
for i in range(1,10):
    if not a%(i*b):
        counter += 1
stdout.write(str(counter))
