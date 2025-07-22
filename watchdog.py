from sys import stdin,stdout

# code runs in O(N*S^2*H)
def can_reach_all_hatches(x,y,hatches,L):
    for a,b in hatches:
        if (a - x) ** 2 + (b - y) ** 2 > L ** 2:
            return False
    return True

def solve_testcase():
    S,H = map(int,stdin.readline().split())
    hatches = {tuple(map(int,stdin.readline().split())) for i in range(H)}
    for x in range(S):
        for y in range(S):
            if (x,y) not in hatches:
                # M = longest possible leash from point (x,y)
                M = min([x,S - x,y,S - y])
                if can_reach_all_hatches(x,y,hatches,M):
                    return f"{x} {y}"
    return "poodle"
                
                
for _ in range(int(stdin.readline())):
    stdout.write(f"{solve_testcase()}\n")
