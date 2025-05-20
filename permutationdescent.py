from sys import stdin,stdout

MOD = 1001113

PDC = [[None for i in range(101)] for j in range(101)]
for i in range(1,101):
    PDC[i][0] = 1
    PDC[i][i - 1] = 1

# to convert a permutation of 1..n-1 to a permutation of 1...n
# n can be inserted in any of the n slots in original permutation
# if n is inserted between two elemnts which form a descent, no new descent is created
# if we add n to the end, no new descent is created
# thus from a permutaion of order n-1 with d descents we get
# d+1 permutations of order n with d descents AND
# n-d-1 permeutations of order n with d+1 descents
# to get a permutation of order n with d descents we can
# take any permutation of order n-1 and d descents and insert n between descents or at the end OR
# take any permutation of order n-1 and d-1 descents and insert n at the begining or not between descent terms
def dp(order, count):
    if count == 0 or count == order - 1:
        return 1
    if PDC[order][count] != None:
        return PDC[order][count]
    PDC[order][count] = ((count + 1) * dp(order - 1, count) + (order - count) * dp(order - 1, count - 1)) % MOD
    return PDC[order][count]

for _ in range(int(stdin.readline())):
    K,N,v = map(int,stdin.readline().split())
    stdout.write(f"{K} {dp(N,v)}\n")
