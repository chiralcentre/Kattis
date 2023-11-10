from itertools import permutations

X = input().strip()
num,ans = int(X),pow(10,9)
X = list(X)
for lst in permutations(X):
    pos = int("".join(lst))
    if pos > num and pos < ans:
        ans = pos
print(ans) if ans != pow(10,9) else print(0)
