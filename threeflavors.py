from sys import stdin

count = [0,0,0]
chars = ["a","b","c"]
s = stdin.readline().strip()
T,M = len(s),0
for c in s:
    p = ord(c) - ord("a")
    count[p] += 1
    M = max(M,count[p])
# it is possible to arrange only if M <= T - M + 1 -> 2 * M - 1 <= T
# assume candy a is most frequent and there are A candies of type a
# hence, there must be A - 1 gaps between consecutive candies of type a
if 2 * M - 1 > T:
    print("IMPOSSIBLE")
else:
    ans = []
    # place most frequently occurring candy first
    while True:
        best = -1
        for i in range(3):
            # ignore same candy type as last candy in sequence
            if count[i] == 0 or (ans and ans[-1] == chars[i]):
                continue
            if best == -1 or count[i] > count[best]:
                best = i
        if best == -1: # cannot be placed
            break
        ans.append(chars[best])
        count[best] -= 1
    print("".join(ans))
            
