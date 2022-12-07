from sys import stdin,stdout

N = int(stdin.readline())
trips = list(map(int,stdin.readline().split()))
unique,total = set(),0
#O(N)
for L in trips:
    total += L
    unique.add(L)
answers = [total - d for d in unique]
answers.sort() #O(N log N) #worst case
stdout.write(f"{len(answers)}\n")
stdout.write(" ".join(str(num) for num in answers))
