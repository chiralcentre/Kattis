s = input().strip()
best = "z" * (len(s) + 1)
# O(N^4) approach, where N is length of string
for i in range(1,len(s) - 1):
    for j in range(i + 1, len(s)):
        ns = s[:i][::-1] + s[i:j][::-1] + s[j:][::-1]
        if ns < best:
            best = ns
print(best)
