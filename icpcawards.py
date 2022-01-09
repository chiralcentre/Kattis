winners = {}
for _ in range(int(input())):
    school,team = input().split()
    if school not in winners and len(winners) < 12:
        winners[school] = team

for key,value in winners.items():
    print(f'{key} {value}')
    
