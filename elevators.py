d,n = input().split()
n = int(n)
if d == "residential":
    if n == 1:
        print(0)
    elif 2 <= n <= 5:
        print(1)
    elif 6 <= n <= 10:
        print(2)
    elif 11 <= n <= 15:
        print(3)
    else:
        print(4)
elif d == "commercial":
    if n == 1:
        print(0)
    elif 2 <= n <= 7:
        print(1)
    elif 8 <= n <= 14:
        print(2)
    else:
        print(3)
else:
    if n == 1:
        print(0)
    elif 2 <= n <= 4:
        print(1)
    elif 5 <= n <= 8:
        print(2)
    elif 9 <= n <= 12:
        print(3)
    elif 13 <= n <= 16:
        print(4)
    else:
        print(5)
    
