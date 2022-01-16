first = True
while True:
    n = int(input())
    if n == 0:
        break
    if first:
        first = False
    else:
        print()
    lst1,lst2 = [int(input()) for _ in range(n)],[int(input()) for _ in range(n)]
    s1,s2 = sorted(lst1),sorted(lst2)
    dict1 = {s1[i]: s2[i] for i in range(n)}
    for num in lst1:
        print(dict1[num])
