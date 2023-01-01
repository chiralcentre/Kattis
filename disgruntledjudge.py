from sys import stdin,stdout

#brute force through all possible values of a and b from 0 to 10000
def solve(odd):
    pairs = []
    if len(odd) == 1:
        return [(1,1)]
    for a in range(10001):
        for b in range(10001):
            if (a * ((a * odd[0] + b) % 10001) + b) % 10001 == odd[1]:
                pairs.append((a,b))
    for i in range(1,len(odd) - 1):
        temp = []
        for a,b in pairs:
            if (a * ((a * odd[i] + b) % 10001) + b) % 10001 == odd[i+1]:
                temp.append((a,b))
        pairs = temp  
    return temp

odd = [int(stdin.readline()) for _ in range(int(stdin.readline()))]
a,b = solve(odd)[0]
for num in odd:
    stdout.write(f"{((a*num + b)%10001)}\n")
