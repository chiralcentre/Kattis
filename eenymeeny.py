def print_team(team):
    print(len(team))
    for member in team:
        print(member)

length = len(input().split())
kids = [input().strip() for i in range(int(input()))]
team1,team2 = [],[]

nxt = 0
while kids:
    index = (nxt+length-1)%len(kids)
    temp = kids[(index+1)%len(kids)]
    team1.append(kids[index]) if len(team1) <= len(team2) else team2.append(kids[index])
    kids.pop(index)
    if len(kids) > 0:
        nxt = kids.index(temp)

print_team(team1)
print_team(team2)
