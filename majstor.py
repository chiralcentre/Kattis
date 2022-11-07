from sys import stdin,stdout

win = {"S":"P","P":"R","R":"S"}
R = int(stdin.readline())
sven = stdin.readline().strip()
N = int(stdin.readline())
friends = [stdin.readline().strip() for _ in range(N)]
actual_score,highest_score = 0,0
for i in range(R):
    freq = {}
    for j in range(N):
        f = friends[j]
        actual_score += 2 if win[sven[i]] == f[i] else 1 if sven[i] == f[i] else 0
        freq[f[i]] = 1 if f[i] not in freq else freq[f[i]] + 1
    possibilities = ["S","P","R"]
    highest = 0
    for p in possibilities:
        temp = 0
        for key,value in freq.items():
            temp += 2 * value if win[p] == key else value if p == key else 0
        highest = max(temp,highest)
    highest_score += highest
stdout.write(f"{actual_score}\n")
stdout.write(f"{highest_score}\n")
        
