from sys import stdin

def parse_class(interval):
    a,b = interval.split("-")
    sh,sm = map(int,a.split(":"))
    eh,em = map(int,b.split(":"))
    return (sh * 60 + sm, eh * 60 + em)

n = int(stdin.readline())
wait = pow(10,9)
for _ in range(n):
    schedule = list(map(parse_class,stdin.readline().split()))
    total = sum(schedule[i][0] - schedule[i - 1][1] for i in range(1,len(schedule)))
    wait = min(wait,total)
print(wait)
