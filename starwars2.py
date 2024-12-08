from sys import stdin,stdout

n = int(stdin.readline())
lst = sorted(map(int,stdin.readline().split()))
S = n // 3
for i in range(S):
    lst[i],lst[i + S] = lst[i + S],lst[i]
stdout.write(" ".join(str(num) for num in lst))
stdout.write("\n")
