from sys import stdin,stdout

s = stdin.readline().strip("\n")
c = stdin.readline().strip("\n")
assert len(c) == 1
for i in range(len(s)):
    if s[i] == c:
        stdout.write(f"{i}\n")
        
