def digitsum(n):
    return sum(map(int,list(n)))

def lowest_num(L,ds):
    # end off with largest digit possible
    lst,t = [],ds - 1
    for i in range(L - 1):
        lst.append(min(9,t))
        t -= min(9,t)
    lst.append(1 + t)
    return "".join(map(str,lst[::-1]))

def highest_num(L,ds):
    # start off with highest digit possible
    lst,t = [],ds
    for i in range(L):
        lst.append(min(9,t))
        t -= min(9,t)
    return "".join(map(str,lst))       

N = input().strip()
L,ds = len(N),digitsum(N)
print(f"{lowest_num(L,ds)} {highest_num(L,ds)}\n")
