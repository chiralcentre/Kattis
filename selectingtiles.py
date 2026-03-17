from sys import stdin

INF = pow(10,9)
def can_form_word(freq,target_freq):
    for key,value in target_freq.items():
        if key not in freq or freq[key] < value:
            return False
    return True

# code runs in O(N) time when N is length of first
# note that dictionary comparisons can be taken to run in constant time since there are at most 26 keys
first = stdin.readline().strip()
second = stdin.readline().strip()
target_freq = {}
for char in second:
    target_freq[char] = target_freq.get(char,0) + 1
# sliding window [L, R] inclusive
L,R = 0,0
freq = {}
ans = INF
while R < len(first):
    # expand
    freq[first[R]] = freq.get(first[R], 0) + 1
    # shrink when valid
    while can_form_word(freq, target_freq):
        ans = min(ans, R - L + 1)
        freq[first[L]] -= 1
        L += 1
    R += 1
print(ans if ans != INF else -1)
