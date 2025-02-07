MOD = pow(10,10)
n = int(input())
total = 0
for i in range(1,n + 1):
    total += pow(i,i,MOD)
    total %= MOD
print(total)