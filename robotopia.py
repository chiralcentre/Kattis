from sys import stdin,stdout

def solve(l1,a1,l2,a2,lt,at):
    m1 = min(lt//l1,at//a1)
    m2 = min(lt//l2,at//a2)
    if m1 == 0 or m2 == 0:
        return "?"
    s1,s2 = -1,-1
    for i in range(1, m1 + 1):
        r1 = lt - i * l1
        r2 = at - i * a1
        if not r1 % l2 and not r2 % a2 and r1 // l2 == r2 // a2 and r1 // l2 > 0:
            if s1 == -1 and s2 == -1:
                s1,s2 = i,r1 // l2
            else:
                return "?"
    if s1 > -1 and s2 > -1:
        return f"{s1} {s2}"
    return "?"
    
for _ in range(int(stdin.readline())):
    l1,a1,l2,a2,lt,at = map(int,stdin.readline().split())
    stdout.write(f"{solve(l1,a1,l2,a2,lt,at)}\n")
    
