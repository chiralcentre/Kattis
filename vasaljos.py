# reference: https://math.stackexchange.com/questions/3115018/we-have-n-charged-and-n-uncharged-batteries-and-a-radio-which-needs-two-char
# minimum number of tries required is n / 2 + 3 for n >= 6
# 6 + (n - 6) / 2 = n / 2 + 3
def solve():
    n = int(input())
    pairs = []
    if n == 4: 
        pairs = [(1,2),(3,4),(1,3),(1,4),(2,3),(2,4)]
    else:
        pairs = [(1,2),(1,3),(2,3),(4,5),(5,6),(4,6)]
        for i in range(7,n + 1,2):
            pairs.append((i,i + 1))
    for a,b in pairs:
        print(f"{a} {b}")
        if input().strip() == "Ljos!":
            return

if __name__ == "__main__":
    solve()
