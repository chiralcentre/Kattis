from sys import stdin,stdout

EPSILON = pow(10,-8)

def time_taken(c,d,s):
    return sum(d[i] / (s[i] + c) for i in range(len(d)))

n,t = map(int,stdin.readline().split())
d,s,L = [],[],100000
for i in range(n):
    a,b = map(int,stdin.readline().split())
    d.append(a)
    s.append(b)
    L = min(L,b)
#maximum possible value is 10^6 + 1000 for c
L,H = -L,10000000
while H - L > EPSILON: #absolute error allowed of less than 10^-6
    m = (L + H) / 2
    T = time_taken(m,d,s)
    if T > t:
        L = m
    else:
        H = m
stdout.write(f"{(H + L) / 2}\n")
