a,b,c = map(int,input().split())
intermediate = [a + b, a - b, a * b]
if not a % b:
    intermediate.append(a // b)
smallest = 10**9
for d in intermediate:
    i1 = d + c
    i2 = d - c
    i3 = d * c
    i4 = 10**9 if d % c else d // c
    for num in [i1,i2,i3,i4]:
        if 0 <= num < smallest:
            smallest = num
print(smallest)
