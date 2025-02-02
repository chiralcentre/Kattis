from sys import stdin,stdout

# to take complement, swap accepting states with non accepting states
n,c,s,f = map(int,stdin.readline().split())
stdout.write(f"{n} {c} {s} {n - f}\n")
stdout.write(stdin.readline())
final = set(map(int,stdin.readline().split()))
new_final = [i for i in range(1, n + 1) if i not in final]
stdout.write(" ".join(str(num) for num in new_final))
stdout.write("\n")
for i in range(n):
    stdout.write(stdin.readline().strip())
    stdout.write("\n")
