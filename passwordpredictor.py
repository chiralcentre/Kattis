from sys import stdin

# code runs in O(ltg) time)
L = int(stdin.readline())
t = int(stdin.readline())
tried = []
for _ in range(t):
    guess,s = stdin.readline().split()
    s = int(s)
    tried.append((guess,s))
possible = 0
for _ in range(int(stdin.readline())):
    line = stdin.readline().strip()
    for guess,s in tried:
        score = sum(guess[i] == line[i] for i in range(L))
        if score != s:
            break
    else:
        possible += 1
print(possible)
            
