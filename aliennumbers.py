from sys import stdin,stdout

for j in range(int(stdin.readline())):
    n,s,t = stdin.readline().split()
    b1,b2 = len(s),len(t)
    source = {s[i]: i for i in range(b1)}
    target = [t[i] for i in range(b2)]
    #convert alien number to decimal representation
    dec = sum(source[n[i]] * pow(b1, len(n) - i - 1) for i in range(len(n)))
    ans = []
    #convert to new base
    while dec > 0:
        ans.append(target[dec % b2]) if dec % b2 else ans.append(target[0]) 
        dec //= b2
    stdout.write(f"Case #{j + 1}: ")
    stdout.write("".join(ans[i] for i in range(len(ans) - 1, -1, -1)))
    stdout.write("\n")
