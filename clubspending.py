from sys import stdin,stdout

N = int(stdin.readline())
cumulative = {}
for i in range(N):
    club,spent = stdin.readline().split()
    spent = spent[1:].split(".") # remove dollar sign
    amount = int(spent[0]) * 100 + int(spent[1])
    cumulative[club] = cumulative.get(club,0) + amount
    dollars = str(cumulative[club] // 100)
    cents = str(cumulative[club] % 100).zfill(2)
    stdout.write(f"{club} ${dollars}.{cents}\n")
