from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    stdin.readline() #read in blank line
    N = int(stdin.readline()); teams = []
    for i in range(N):
        #name of team is not needed
        preference = int(stdin.readline().split()[1])
        teams.append(preference)
    teams.sort() #sort by order preference in O(N log N) time
    badness = sum(abs(j + 1 - teams[j]) for j in range(N)) #O(N)
    stdout.write(f"{badness}\n")
