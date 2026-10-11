from sys import stdin,stdout

def check(f):
    L,R = 0,len(f) - 1
    while L <= R:
        if f[L] == "d":
            if L < R and f[R] == "d":
                L += 1
                R -= 1
            else:
                return "counterfeit"
        elif f[L] == "s":
            if L + 1 <= R and f[L + 1] == "s": # bounds check before indexing
                L += 2
            else:
                return "counterfeit"
        elif f[L] == "r":
            L += 1
        elif f[L] == "h":
            return "counterfeit" if L != R else "authentic"
        else:
            return "counterfeit"
    return "counterfeit" # no h was reached
        
for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    if len(s) < 4 or s[0] != "b" or s[-2:] != "cc":
        stdout.write("counterfeit\n")
    else:
        # remove first and last two characters
        stdout.write(f"{check(s[1:-2])}\n")
