from sys import stdin,stdout

def solve(a,b,n,m,k):
    a_wins,b_wins = 0,0
    for i in range(n):
        if a[i] > b[i]:
            a_wins += 1
        elif a[i] < b[i]:
            b_wins += 1
    for i in range(m):
        if a[i] > b[i]:
            a_wins -= 1
        elif a[i] < b[i]:
            b_wins -= 1
        a[i] += k
        if a[i] > b[i]:
            a_wins += 1
        elif a[i] < b[i]:
            b_wins += 1
    if a_wins > b_wins:
        return "0"
    for i in range(n - m + 1):
        if a_wins > b_wins:
            return str(i)
        if a[i] > b[i]:
            a_wins -= 1
        elif a[i] < b[i]:
            b_wins -= 1
        a[i] -= k
        if a[i] > b[i]:
            a_wins += 1
        elif a[i] < b[i]:
            b_wins += 1
        if a[i + m - 1] > b[i + m - 1]:
            a_wins -= 1
        elif a[i + m - 1] < b[i + m - 1]:
            b_wins -= 1
        a[i + m - 1] += k
        if a[i + m - 1] > b[i + m - 1]:
            a_wins += 1
        elif a[i + m - 1] < b[i + m - 1]:
            b_wins += 1
    return "Neibb"

n,m,k = map(int,stdin.readline().split())
a = list(map(int,stdin.readline().split()))
b = list(map(int,stdin.readline().split()))
print(solve(a,b,n,m,k))
