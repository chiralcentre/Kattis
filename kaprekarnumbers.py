from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    k = int(stdin.readline())
    s = str(k * k)
    for i in range(len(s)):
        left = s[:i]
        right = s[i:]
        L = int(left) if left != "" else 0
        R = int(right) if right != "" else 0
        # right part must be nonzero
        if R == 0:
            continue
        if L + R == k:
            stdout.write("YES\n")
            break
    else:
        stdout.write("NO\n")
    
