from sys import stdin

def is_possible(copy,colours,H):
    for i in range(H):
        u = (H - i) ** 2
        if copy[colours[i]] >= u:
            copy[colours[i]] -= u
        else:
            return False
    return True

# binary search on height in O(N log M) time
if __name__ == "__main__":
    N,M = map(int,stdin.readline().split())
    ducks = list(map(int,stdin.readline().split()))
    colours = list(map(lambda x: int(x) - 1, stdin.readline().split())) # offset by 1 due to zero indexing
    L,H = 0,M
    while L <= H:
        C = L + ((H - L) >> 1)
        copy = [x for x in ducks]
        if is_possible(copy, colours, C):
            L = C + 1
            ans = C
        else:
            H = C - 1
    print(ans)
