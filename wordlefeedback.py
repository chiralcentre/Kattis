s,g = input().strip(),input().strip()
f1 = {}
for i in range(len(s)):
    f1[s[i]] = f1.get(s[i],0) + 1

res = ["" for _ in range(len(s))]
# assign G first
for i in range(len(s)):
    if g[i] == s[i]:
        res[i] = "G"
        f1[s[i]] -= 1
# assign Y and -
for i in range(len(s)):
    if g[i] != s[i]:
        if g[i] not in f1 or f1[g[i]] == 0:
            res[i] = "-"
        else:
            res[i] = "Y"
            f1[g[i]] -= 1
print("".join(res))
