from sys import stdin,stdout

def parse(s):
    d = {}
    i = 0
    while i < len(s):
        c = s[i]
        i += 1
        j = i
        while j < len(s) and not s[j].isalpha():
            j += 1
        if j == i:
            d[c] = 1 if c not in d else d[c] + 1
        else:
            d[c] = int(s[i:j]) if c not in d else d[c] + int(s[i:j])
        i = j
    return d

def solve(d1,d2,k):
    L = pow(10,9)
    for key in d2:
        if key not in d1:
            return 0
        L = min(L,(d1[key] * k) // d2[key])
    return L

s,k = stdin.readline().split(); k = int(k)
t = stdin.readline().strip()
stdout.write(f"{solve(parse(s),parse(t),k)}\n")
