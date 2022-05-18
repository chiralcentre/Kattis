from sys import stdin,stdout

#candidates[a] returns the number of votes for candidate a
candidates = {}
while True:
    name = stdin.readline().strip()
    if name == "***":
        break
    candidates[name] = 1 if name not in candidates else candidates[name] + 1
highest = -1; winners = []
for key,value in candidates.items():
    if value > highest:
        highest = value
        winners = [key]
    elif value == highest:
        winners.append(key)
stdout.write("Runoff!") if len(winners) > 1 else stdout.write(winners[0])
        
