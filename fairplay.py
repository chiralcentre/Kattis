from sys import stdin,stdout

# two dimensional 2-sum
def solve():
    n = int(stdin.readline())
    if n % 2: # not possible for odd number of workers
        return "impossible" 
    skills = {} # skills[(b,p)] =  number of people with skill level of b in billiards and p in pool
    B,P = 0,0
    for _ in range(n):
        b,p = map(int,stdin.readline().split())
        B += b
        P += p
        skills[(b,p)] = skills.get((b,p),0) + 1
    g = n // 2
    if B % g or P % g: # not possible to divide evenly
        return "impossible"
    else:
        ab,ap = B // g, P // g
        for b,p in list(skills.keys()):
            if (b,p) not in skills: # has been popped already
                continue 
            rb,rp = ab - b,ap - p
            if (rb,rp) not in skills:
                return "impossible"
            if (b,p) == (rb,rp):
                if skills[(b,p)] % 2:
                    return "impossible"
                skills.pop((b,p))
            else:
                if skills[(b,p)] != skills[(rb,rp)]:
                    return "impossible"
                skills.pop((b,p))
                skills.pop((rb,rp))
        return "possible"

if __name__ == "__main__":
    print(solve())
