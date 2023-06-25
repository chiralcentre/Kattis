from sys import stdin,stdout

def solve(last,word_endings,possible):
    for p in possible:
        for i in range(len(last)):
            if last[i:] in word_endings[p]:
                return "YES"
    return "NO"

S = stdin.readline().strip()
E = int(stdin.readline())
word_endings = [set(stdin.readline().split()) for _ in range(E)]
possible = []
for i in range(E):
    for j in range(len(S)):
        if S[j:] in word_endings[i]:
            possible.append(i)
            break
for _ in range(int(stdin.readline())):
    line = stdin.readline().split()
    last = line[-1]
    stdout.write(f"{solve(last,word_endings,possible)}\n")
            
