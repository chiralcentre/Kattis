for i in range(int(input())):
    n,m = map(int,input().split())
    stickers = {num: 0 for num in range(1,m+1)}
    prizes = []
    for j in range(n):
        k,*types,value = map(int,input().split())
        prizes.append((types,value))  
    collection = list(map(int,input().split()))
    for k in range(m): 
        stickers[k+1] += collection[k] #offset by 1
    winnings = 0
    for prize in prizes:
        winnings += min(stickers[d] for d in prize[0])*prize[1]
    print(winnings)
        
    
