from sys import stdin,stdout
from math import ceil

ranks = {1: 100, 2: 75, 3: 60, 4: 50, 5: 45, 6: 40, 7: 36, 8: 32, 9: 29, 10: 26,
         11: 24, 12: 22, 13: 20, 14: 18, 15: 16, 16: 15, 17: 14, 18: 13, 19: 12, 20: 11,
         21: 10, 22: 9, 23: 8, 24: 7, 25: 6, 26: 5, 27: 4, 28: 3, 29: 2, 30: 1}
n = int(stdin.readline())
contestants = [list(map(int,stdin.readline().split())) + [i] for i in range(n)]
sorted_c = sorted(contestants,key = lambda x: (-x[0],x[1],x[2]))
scores = [0 for _ in range(n)]
i = 0
while i < n:
    s = ranks[i+1] if i + 1 in ranks else 0
    consec = 1
    while i + 1 < n and sorted_c[i][:3] == sorted_c[i + 1][:3]:
        consec += 1
        i += 1
        if i + 1 in ranks:
            s += ranks[i+1] 
    average = ceil(s / consec)
    for j in range(consec):
        scores[i - j] = average + sorted_c[i - j][3]
    i += 1
for i in range(n):
    sorted_c[i].append(scores[i])
sorted_c.sort(key = lambda x: x[4])
for i in range(n):
    stdout.write(f"{sorted_c[i][5]}\n")
    
        
        
    
    
