problems = input().split(';')
counter = 0
for problem in problems:
    if '-' in problem: #problems are in a range
        a,b = map(int,problem.split('-'))
        counter += b - a + 1
    else:
        counter += 1
print(counter)
