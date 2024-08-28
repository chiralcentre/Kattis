from sys import stdin

n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
lst = [(i + 1, v) for i,v in enumerate(a)]
lst.sort(key=lambda x: -x[1]) # sort in descending order
print(" ".join(str(elem[0]) for elem in lst))
