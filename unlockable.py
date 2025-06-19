from sys import stdin,stdout

# runs in O(N log 10^9) = O(N) time
N,a = stdin.readline().split()
a = int(a)
B = set(map(int,stdin.readline().split()))
unique_pairs = 0
for b in B:
    c,m = a,1
    while c <= b:
        if not b % c:
            unique_pairs += 1
        c *= a
        m += 1
print(unique_pairs)
