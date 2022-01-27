candidates,votes = {},{}
for _ in range(int(input())):
    name,party = input().strip(),input().strip()
    candidates[name] = party

for _ in range(int(input())):
    person = input().strip()
    if person in candidates:
        votes[person] = votes[person] + 1 if person in votes else 1
        
if len(votes) > 0: # if there is valid votes
    highest = max(votes.values())
    print("Tie") if list(votes.values()).count(highest) > 1 else print(candidates[list(votes.keys())[list(votes.values()).index(highest)]])
else:
    print("Tie")
    
