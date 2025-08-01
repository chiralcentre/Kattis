from sys import stdin

n = int(stdin.readline())
prev,curr = stdin.readline().strip(),stdin.readline().strip()
total = 0
for i in range(n):
    d = abs(ord(prev[i]) - ord(curr[i]))
    total += min(d, 26 - d)
print(total)
