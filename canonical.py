from sys import stdin,stdout

INF = pow(10,9)

def solve(coins,n,v):
    dpres,gres = [INF for _ in range(v)],[INF for _ in range(v)]
    dpres[0],gres[0],prev = 0,0,0
    for j in range(1,v):
        while prev < n - 1 and coins[prev + 1] <= j:
            prev += 1
        gres[j] = gres[j - coins[prev]] + 1
        for i in range(n):
            if j - coins[i] >= 0 and dpres[j - coins[i]] + 1 < dpres[j]:
                dpres[j] = dpres[j - coins[i]] + 1
        if dpres[j] != gres[j]:
            return "non-canonical"
    return "canonical"


#overall time complexity is O(nV), where V is the sum of the two largest denominations
n = int(stdin.readline())
coins = list(map(int,stdin.readline().split()))
H = coins[-1] + coins[-2] #take sum of two largest denominations as the upper bound
stdout.write(solve(coins,n,H))
