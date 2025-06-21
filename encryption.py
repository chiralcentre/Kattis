from sys import stdin,stdout

# length of shortest common sequence = |s| + |d| - |LCS|
s,d,LCS = stdin.readline().strip(),stdin.readline().strip(),stdin.readline().strip()
a,b = 0,0
ans = []
for char in LCS:
    # add unmatched LCS characters from s
    while a < len(s) and s[a] != char:
        ans.append(s[a])
        a += 1
    # add unmatched LCS characters from d
    while b < len(d) and d[b] != char:
        ans.append(d[b])
        b += 1
    # add LCS char
    ans.append(char)
    a += 1; b += 1
# add remaining characters
for i in range(a,len(s)):
    ans.append(s[i])
for i in range(b,len(d)):
    ans.append(d[i])
stdout.write("".join(ans))
stdout.write("\n")

    
