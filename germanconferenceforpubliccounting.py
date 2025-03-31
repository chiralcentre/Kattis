n = input().strip()
if len(n) == 1:
    print(int(n) + 1)
else:
    num = int(n)
    base = 10 * (len(n) - 1) + int(n[0])
    if int(n[0] * len(n)) > num:
        base -= 1
    print(base)
