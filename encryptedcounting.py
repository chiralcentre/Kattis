M,S = input().split()
ans = 0
# assume S is always able to be derived from M
while M != S:
    s = ""
    freq = 1
    for i in range(1,len(M)):
        if M[i] == M[i - 1]:
            freq += 1
        else:
            s += str(freq) + M[i - 1]
            freq = 1
    s += str(freq) + M[-1]
    M = s
    ans += 1
print(ans)
