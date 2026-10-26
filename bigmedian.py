from sys import stdin

# is_feasible(x) checks if the array can be split into K odd length segments where every median is >= x
# is_feasible(x) is monotone in x
# Proof: let us assume there is a valid partition P into K odd length segments where every median >= X for a given X
# If is_feasible(X) with parition P, then for any Y <= X, P is a valid partition for Y as well. This means is_feasible(X) -> is_feasible(Y) for all Y <= X
# Similarly, if no valid partition is present for X, then no valid partition will exist for Z >= y. This means ~is_feasible(X) -> ~is_feasible(Z) for all Z >= X
# Let f(x) = -1 if x <= X else 1
# Apply f(x) on the given array
# Now, is_feasible(x) is checking if the array can be split into K odd length segments with positive sum (since positive sum means median of the segment >= X)
# Naively, we can use a greedy solution to carve out M >= K odd length segments where this occurs
# Now, we have to prove that at least K segments exist means that exactly K segments exist
# We can do this by keeping greedy segments 1 to K - 1 as they are, and glue everything else together into one final segment: pieces K,K + 1,...,M, and a tail stuck onto the end
# These new K segments cover the whole array. Segments 1 to K - 1 are legal by construction
# Now, we need to look into when the last new segment is legal
# Sum of the final segment, S = (M - K + 1) + T, where T is sum of tail
# S = (M + T) - K + 1 = B - K + 1, where B was sum of the original array
# if S >= 1, last segment is legal -> B - K + 1 >= 1 -> B >= K
# Now we have proven that if B >= K, a valid K partition exists
# In the other direction, if a valid K partition exists, each segment has a minimum sum of 1, so their total sum is at least K -> B >= K
# Valid K partition exists <-> B >= K
def is_feasible(arr,K,x):
    B = sum(1 if num >= x else -1 for num in arr)
    return B >= K

# code runs in O(N) time
N,K = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))
L,H = pow(10,18),-1
for num in arr:
    L = min(num,L)
    H = max(num,H)
while L <= H:
    M = L + ((H - L) >> 1)
    if is_feasible(arr,K,M):
        L = M + 1
    else:
        H = M - 1
print(H)
