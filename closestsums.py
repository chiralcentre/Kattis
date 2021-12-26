import sys

line = lambda : sys.stdin.readline().strip()
n = line()
case = 1
while n:
    n = int(n)
    nums = [int(input()) for i in range(n)]
    sums = sorted([nums[i] + nums[j] for i in range(n) for j in range(i+1,n)])
    m = int(line())
    queries = [int(input()) for j in range(m)]
    print(f'Case {case}: ')
    for query in queries:
        if query <= sums[0]:
            print(f'Closest sum to {query} is {sums[0]}.')
        else:
            for i in range(1,len(sums)):
                if query < sums[i]:
                    break
            print(f'Closest sum to {query} is {sums[i]}.') if sums[i] - query < query - sums[i-1] else print(f'Closest sum to {query} is {sums[i-1]}.')
    case += 1
    n = line()
        
