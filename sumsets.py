from sys import stdin,stdout

def solve(elems):
    #generate all pairs of a + b in O(N^2) time, and sort in O(N^2 log N^2) time
    mappings = {}
    for i in range(len(elems)):
        for j in range(i + 1, len(elems)):
            s = elems[i] + elems[j]
            #only need to keep track of one (i,j) pair such that elems[i] + elems[j] == s
            mappings[s] = 4000 * i + j
    #generate all pairs of d - c in O(N^2) time
    ans = -pow(10,9)
    for i in range(len(elems)):
        for j in range(i + 1, len(elems)):
            d1 = elems[j] - elems[i]
            d2 = elems[i] - elems[j]
            if d1 in mappings:
                h = mappings[d1]
                #found four distinct elements
                if len({h // 4000, h % 4000, i, j}) == 4:
                    ans = max(ans, elems[j])
            if d2 in mappings:
                h = mappings[d2]
                #found four distinct elements
                if len({h // 4000, h % 4000, i, j}) == 4:
                    ans = max(ans, elems[i])            
    return "no solution" if ans == -pow(10,9) else str(ans)

N = int(stdin.readline())
elems = [int(stdin.readline()) for _ in range(N)]
stdout.write(f"{solve(elems)}\n")


