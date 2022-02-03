N,T,K = map(int,input().split())
deck,prices = {num: 0 for num in range(1,T+1)},{}
for card in list(map(int,input().split())):
    deck[card] += 1
for i in range(T):
    buy,sell = map(int,input().split())
    # For each card type, the "net cost" of making a combo is the cost for buying missing cards plus the loss of profit for not selling cards of that type.
    prices[i+1] = (buy,sell,max(2-deck[i+1],0)*buy + deck[i+1]*sell)
    
# optimal combination should have lowest net cost
# sell T-K card types with higher net cost, and buy K card types with lower net cost
prices = sorted(prices.items(), key = lambda x: x[1][2])
profit = 0
for _ in range(T-K):
    card,nums = prices.pop()
    profit += deck[card]*nums[1] #selling
for _ in range(K):
    card,nums = prices.pop()
    if deck[card] <= 2:
        profit -= (2-deck[card])*nums[0] #buying
    else:
        profit += (deck[card]-2)*nums[1] #selling
print(profit)
    
