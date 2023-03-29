from sys import stdin,stdout

NAME = "ThoreHusfeldt"
def solve(scoreboard,index):
    if index == 0:
        return "Thore is awesome"
    else:
        #check if there is another person with name containing ThoreHusfeld as a prefix
        for i in range(index):
            if scoreboard[i].startswith("ThoreHusfeld"):
                return "Thore sucks"
        for i in range(1,len(NAME) + 1):
            prefix = NAME[:i]
            determine = True
            for j in range(index):
                if scoreboard[j].startswith(prefix):
                    determine = False
                    break
            if determine:
                return prefix
                  
n = int(stdin.readline())
scoreboard,index = [],-1
for i in range(n):
    name = stdin.readline().strip()
    scoreboard.append(name)
    if name == NAME:
        index = i
stdout.write(f"{solve(scoreboard,index)}\n")
