from sys import stdin,stdout

S = int(stdin.readline())
solutions = []
for i in range(2, S//2 + 2):
    m1 = S // (2*i - 1)
    if m1 * (2 * i - 1) == S or m1 * (2 * i - 1) + i == S:
        solutions.append((i,i - 1))
    m2 = S // (2*i)
    if m2 * 2 * i == S or m2 * 2 * i + i == S:
        solutions.append((i,i))  
stdout.write(f"{S}:\n")
for x,y in solutions:
    stdout.write(f"{x},{y}\n")
