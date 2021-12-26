money = 100
prev = 1000 #arbitarily large number since price cannot exceed 500

for i in range(int(input())):
    current = int(input())
    if current > prev:
        money += min((money//prev),100000)*(current-prev) #if current price > previous price, there is a gain
    prev = current
print(money)
