n = int(input())
found = False
n += 1
while not found:
    prod = n * n
    if "6" not in str(prod):
        print(n)
        found = True
    n += 1
