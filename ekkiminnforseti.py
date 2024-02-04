from sys import stdin,stdout
INF = pow(10,9)
# O(nm) time
n,m = map(int,stdin.readline().split())
candidates = [stdin.readline().strip() for _ in range(m)]
removed = [False for _ in range(m)]
# reverse order of votes to pop from back
votes = [list(map(lambda x: int(x) - 1,stdin.readline().split()))[::-1] for _ in range(n)]
winner,loser,best,lowest,freq = -1,-1,-1,INF,{i: 0 for i in range(m)}
# while winner is not found
while winner < 0:
    for lst in votes:
        while removed[lst[-1]]:
            lst.pop()
        freq[lst[-1]] += 1
    L = set()
    for key,value in freq.items():
        if value > 0:
            if value > best:
                winner,best = key,value
            elif value == best and key < winner:
                winner = key
            if value < lowest:
                loser,lowest = key,value
            elif value == lowest and key > loser:
                loser = key
        else:
            L.add(key)
    if (best << 1) <= n:
        L.add(loser)
        for key in L:
            removed[key] = True
            del freq[key]
        for key in freq:
            freq[key] = 0
        winner,loser,best,lowest = -1,-1,-1,INF
stdout.write(f"{candidates[winner]}\n")


