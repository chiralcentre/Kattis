from sys import stdin,stdout

C = int(stdin.readline())
current_holdings = [0 for _ in range(C)]
company_records = [{} for _ in range(C)]
days = set()
for i in range(C):
    K = int(stdin.readline())
    for j in range(K):
        N,D = map(int,stdin.readline().split())
        company_records[i][D] = N
        days.add(D) # add all unique days

days = sorted(list(days)) #O(n log n) where n = number of days
for k in range(len(days)): #O(nC) where n is number of days
    D = days[k]
    for m in range(C):
        if D in company_records[m]:
            current_holdings[m] = company_records[m][D]
    stdout.write(f'{sum(current_holdings)} ') if k < len(days) - 1 else stdout.write(f'{sum(current_holdings)}')
    
