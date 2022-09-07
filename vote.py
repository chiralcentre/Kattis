from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    votes,total = [],0
    highest,winners = -1,[]
    for i in range(n):
        v = int(stdin.readline())
        votes.append(v)
        total += v
        if v > highest:
            highest = v
            winners = [i+1]
        elif v == highest:
            winners.append(v)
    if len(winners) > 1:
        stdout.write("no winner\n")
    elif highest > total//2:
        stdout.write(f"majority winner {winners[0]}\n")
    elif highest <= total//2:
        stdout.write(f"minority winner {winners[0]}\n")
