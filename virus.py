from sys import stdin,stdout

#beginning and end of the two strings should be identical up till the change
s1,s2 = stdin.readline().strip(),stdin.readline().strip()
L = min(len(s1),len(s2))
i = -1
for k in range(L):
    i = k
    if s1[k] != s2[k]:
        break
L -= i
j = L
for k in range(L):
    if s1[len(s1) - k - 1] != s2[len(s2) - k - 1]:
        j = k
        break
stdout.write(f"{len(s2) - i - j}\n")
