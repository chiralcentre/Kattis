from sys import stdin,stdout

# highest number is a 7 for first or second rounds
def find_winner(a,b,r):
    if r < 2 and max(a,b) > 7:
        return -1
    if (a >= 6 and a - b >= 2) or (a == 7 and b == 6 and r < 2):
        return 0
    if (b >= 6 and b - a >= 2) or (b == 7 and a == 6 and r < 2):
        return 1
    return -1

def check_valid(sets,names):
    if len(sets) > 3: #takes at most three sets to find winner
        return "ne"
    won = [0,0]
    for i in range(len(sets)):
        if won[0] == 2 or won[1] == 2:
            return "ne"
        a,b = map(int,sets[i].split(":"))
        w = find_winner(a,b,i)
        if w == -1 or names[1 - w] == "federer":
            return "ne"
        won[w] += 1
    return "da" if won[0] >= 2 or won[1] >= 2 else "ne"

names = stdin.readline().split()
N = int(stdin.readline())
for i in range(N):
    sets = stdin.readline().split()
    stdout.write(f"{check_valid(sets,names)}\n")
