C,L = float(input()),int(input())
areas = [(lambda x: float(x[0])*float(x[1]))(input().split()) for _ in range(L)]
print(sum(area*C for area in areas))
