from sys import stdin,stdout

N,P,K = int(stdin.readline()),int(stdin.readline()),int(stdin.readline())
cost = list(map(int,stdin.readline().split()))
categories = list(map(int,stdin.readline().split()))
pastry_cost = sorted([(cost[i],categories[i]) for i in range(N)])
bought,spent,ans = {},0,0
for c,t in pastry_cost:
    if spent + c <= P:
        curr = bought.get(t,0)
        if curr < K:
            bought[t] = curr + 1
            spent += c
            ans += 1
    else:
        break
stdout.write(f"{ans}\n")
        

