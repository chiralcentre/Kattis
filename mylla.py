from sys import stdin

def solve(results,N):
    scores = {"H": 0, "A": 0}
    i = 0
    while i < len(results):
        temp = {"H": 0, "A": 0}
        j = i
        while temp["H"] < 3 and temp["A"] < 3:
            temp[results[j]] += 1
            j += 1
        if temp["H"] > temp["A"]:
            scores["H"] += 1
        else:
            scores["A"] += 1
        if scores["H"] == N:
            return "Arnar"
        if scores["A"] == N:
            return "Hannes"
        i = j
        
N = int(stdin.readline())
results = stdin.readline().strip()
print(solve(results,N))
