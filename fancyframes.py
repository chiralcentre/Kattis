a,b,c,d = input().split()
c,d = int(c),int(d)
if c == 0: # frame and gap are both 0
    print(a)
else:
    L = len(a) + 2 * d + 2 * c
    for i in range(c):
        print(b * L)
    for i in range(d):
        print(b * c, end = "")
        print(" " * (L - 2 * c), end = "")
        print(b * c)
    print(b * c + " " * d, end = "")
    print(a,end = "")
    print(" " * d + b * c)
    for i in range(d):
        print(b * c, end = "")
        print(" " * (L - 2 * c), end = "")
        print(b * c)
    for i in range(c):
        print(b * L)
