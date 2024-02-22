from sys import stdin,stdout

# O(n^2)
n = int(stdin.readline())
# maximum word length is 20
words = [[] for _ in range(21)]
for _ in range(n):
    w = stdin.readline().strip()
    words[len(w)].append(w)
ans = 0
# minimum 3 words, maximum 20 words
for k in range(3,21):
    hints = {}
    for i in range(len(words[k])):
        for j in range(i + 1,len(words[k])):
            s,e = 0,k - 1
            while s < k and words[k][i][s] == words[k][j][s]:
                s += 1
            while e >= 0 and words[k][i][e] == words[k][j][e]:
                e -= 1
            # position of consecutive letters, actual consecutive letters, length of original word all matter
            if e - s == 1:
                h = "".join(sorted([words[k][i][s:e+1],words[k][j][s:e+1]]))
                hints[(h,s)] = hints.get((h,s),0) + 1
    ans += sum(v == 1 for k,v in hints.items())
stdout.write(f"{ans}\n")
