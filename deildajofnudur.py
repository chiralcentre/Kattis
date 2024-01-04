from sys import stdin,stdout

def equal_departments(freq):
    return len(set(freq.values())) == 1

n = int(stdin.readline())
grants = stdin.readline().strip()
best = -1
#O(n^3)
for i in range(n):
    freq = {}
    for j in range(i,n):
        freq[grants[j]] = freq.get(grants[j],0) + 1
        if equal_departments(freq):
            best = max(best,len(freq) * freq[grants[j]])
stdout.write(f"{best}\n")
