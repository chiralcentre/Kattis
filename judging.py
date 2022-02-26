from sys import stdin,stdout

n = int(stdin.readline())
DOMjudge,Kattis,common = {},{},set()
for i in range(n):
    judgement = stdin.readline().strip()
    DOMjudge[judgement] = DOMjudge[judgement] + 1 if judgement in DOMjudge else 1
for j in range(n):
    judgement = stdin.readline().strip()
    if judgement in DOMjudge:
        common.add(judgement)
    Kattis[judgement] = Kattis[judgement] + 1 if judgement in Kattis else 1

counter = 0
for judgement in common:
    counter += min(DOMjudge[judgement],Kattis[judgement])
stdout.write(f'{counter}\n')
