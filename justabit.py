s = input().strip()
a,b = 0,0
for char in s:
    if char == "0":
        a += 1
    else:
        b += 1
print(f"{a} {b}")
