K = int(input())
coins = 0
#K is a multiple of 100, and can be filled in exact
if not K%100:
    while K > 0:
        if K < 100:
            K = 0
        elif 100 <= K < 200:
            K -= 100
        elif 200 <= K < 500:
            K -= 200
        else:
            K -= 500
        coins += 1
else:
    while K > 0:
        if K >= 500:
            K -= 500
        else:
            if 200 <= K <= 400:
                coins += 2
                break
            else:
                coins += 1
                break
        coins += 1
print(coins)
