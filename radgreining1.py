from sys import stdin,stdout

# worst case O(nm) time complexity
def solve():
    n,m = map(int,stdin.readline().split())
    seq = ["" for _ in range(n)]
    for i in range(m):
        s,sect = stdin.readline().split()
        s = int(s) - 1 # offset by 1 due to zero indexing
        for j in range(s,s + len(sect)):
            if seq[j] == "":
                seq[j] = sect[j - s]
            elif seq[j] != sect[j - s]:
                return "Villa"
    for i in range(n):
        if seq[i] == "":
            seq[i] = "?"
    return "".join(seq)

stdout.write(solve())
