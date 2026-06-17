from sys import stdin

def simplex(c, A, b):
    m, n = len(b), len(c)
    total = n + m
    tableau = [[0.0] * (total + 1) for _ in range(m + 1)]
    for j in range(n):
        tableau[0][j] = -c[j]
    for i in range(m):
        for j in range(n):
            tableau[i+1][j] = A[i][j]
        tableau[i+1][n+i] = 1.0
        tableau[i+1][total] = b[i]

    while True:
        pivot_col = min(range(total), key=lambda j: tableau[0][j])
        if tableau[0][pivot_col] >= -1e-9:
            break
        ratios = [
            (tableau[i][total] / tableau[i][pivot_col], i)
            for i in range(1, m+1) if tableau[i][pivot_col] > 1e-9
        ]
        pivot_row = min(ratios)[1]
        pv = tableau[pivot_row][pivot_col]
        tableau[pivot_row] = [x / pv for x in tableau[pivot_row]]
        for i in range(m+1):
            if i != pivot_row:
                f = tableau[i][pivot_col]
                tableau[i] = [tableau[i][j] - f * tableau[pivot_row][j] for j in range(total+1)]

    return tableau[0][total]

def main():
    m,n = map(int,stdin.readline().split())
    metals = list(map(int,stdin.readline().split()))
    percentages, profits = [], []
    for j in range(n):
        line = list(map(float,stdin.readline().split()))
        profits.append(line[-1])
        percentages.append(line[:-1])
    A = [[percentages[j][i]/100.0 for j in range(n)] for i in range(m)]
    return f"{simplex(profits, A, metals):.2f}"

print(main())
