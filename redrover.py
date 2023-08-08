def naiveMatching(T, P):
    i,freq = 0,0
    while i < len(T):
        found = True
        for j in range(len(P)):
            if not found:
                break
            if i + j >= len(T) or P[j] != T[i + j]:
                found = False
        if found:
            freq += 1
        i += len(P) if found else 1
    return freq

S = input().strip()
ans = len(S)
# brute force every possible pattern in O(N^3) time, where N is length of string
for i in range(len(S)):
    for j in range(i + 1,len(S)):
        m = naiveMatching(S,S[i:j])
        ans = min(ans, len(S) - (j - i - 1) * m + j - i)
print(ans)
