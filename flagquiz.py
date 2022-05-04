from sys import stdin,stdout

stdin.readline() #read in question
N = int(stdin.readline())
answers = [stdin.readline().strip().split(", ") for i in range(N)]
#changes[a] stores the maximum number of changes required to transform answers[a] into any of the alternatives
changes = [0 for i in range(N)]
for i in range(N): #O(N^2)
    for j in range(i+1,N):
        counter = sum(answers[i][k] != answers[j][k] for k in range(len(answers[i])))
        changes[i] = max(counter,changes[i]); changes[j] = max(counter,changes[j])
lowest = min(changes) #O(N)
for i in range(N): #O(N)
    if changes[i] == lowest:
        stdout.write(", ".join(answers[i])+'\n')
