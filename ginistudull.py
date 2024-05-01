from sys import stdin

n = int(stdin.readline())
incomes = sorted([int(stdin.readline()) for _ in range(n)])
# cancel out common factor of 2
denom = sum(incomes) * n
numerator = sum(i * incomes[i] - (n - 1 - i) * incomes[i] for i in range(n))
print(numerator/denom)
