from sys import stdin

def canBeatTimeLimit(rate,T,word_count):
    curr_words,total = 0,0
    for w in word_count:
        curr_words += w
        total += curr_words // rate
        if total >= T:
            return False
    return total < T

# perform binary search
# maximum w is 10^9, maximum total is 10^14, set upperbound as 10^15
# runs in O(n log n + n)= O(n log n) time
n,T = map(int,stdin.readline().split())
# solve shorter questions first
word_count = sorted(map(int,stdin.readline().split()))
L,H,ans = 1,pow(10,15),None
while L <= H:
    M = L + ((H - L) >> 1)
    if canBeatTimeLimit(M,T,word_count):
        ans = M
        H = M - 1
    else:
        L = M + 1
print(ans)
