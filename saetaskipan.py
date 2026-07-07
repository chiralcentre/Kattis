M,F,N = int(input()),int(input()),int(input())
H,T = max(M,F,N),M + F + N
# it is possible to arrange only if H <= T - H + 1 -> 2 * H - 1 <= T
# assume boys are most frequent and there are H boys
# hence, there must be H - 1 gaps between consecutive boys
if 2 * H - 1 > T:
    print("O nei!")
else:
    freq = [M,F,N]
    chars = ["M","F","N"]
    ans = []
    # place most frequent friend types first
    while True:
        best = -1
        for i in range(3):
            if (freq[i] == 0) or (ans and ans[-1] == chars[i]):
                continue
            if best == -1 or freq[i] > freq[best]:
                best = i
        if best == -1: # can no longer be placed
            break
        ans.append(chars[best])
        freq[best] -= 1
    print("".join(ans))
