from sys import stdin,stdout

s,i = stdin.readline(),0
while i < len(s):
    stdout.write(s[i])
    j = i + 1
    while j < len(s) and s[j] == s[i]:
        j += 1
    i = j
