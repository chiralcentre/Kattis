# rough upper bound is 16^15 -1
L,H = 0,(1 << 60) - 1
while L <= H:
    M = (L + H) >> 1
    num = hex(M)[2:].upper().zfill(15) #remove leading 0x and fill with leading zeroes up to 15
    print(f"? {num}", flush = True)
    response = input().strip()
    if response == "Too high!":
        H = M - 1
    elif response == "Too low!":
        L = M + 1
    else:
        exit(0)
