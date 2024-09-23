from sys import stdin,stdout

# generate all possible substrings in O(N^3) time where N is length of string
S = stdin.readline().strip()
freq = {}
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        substr = S[i:j]
        freq[substr] = freq.get(substr, 0) + 1
for key, value in sorted(freq.items(), key = lambda x: (-x[1], x[0])):
    stdout.write(f"{value} {key}\n")
