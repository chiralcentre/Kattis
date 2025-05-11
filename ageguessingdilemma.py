B = int(input())
L,H = 1,pow(10,9)
while L <= H:
    # bias factor of 1 / B + 1 to make the guess lower if the penalty is higher
    M = L + int((H - L) * (1 / (B + 1)))
    print(M)
    res = input().strip()
    if res == "lower":
        H = M - 1
    elif res == "higher":
        L = M + 1
    else:
        break
