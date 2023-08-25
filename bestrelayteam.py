sprinters,best_team,n = [],[],int(input())
for _ in range(n):
    name,t1,t2 = input().split()
    sprinters.append((name,float(t1),float(t2)))
# sort by fastest flying start timing first
sprinters = sorted(sprinters,key = lambda x: x[2])
lowest_time = 9999999999 # arbitrarily large number
# try every runner on first leg and fill up the team with the fastest three remaining flying start timings
for i in range(n):
    counter,team = sprinters[i][1],[]
    team.append(sprinters[i][0])
    if i <= 2: # choosing from below top three in flying start rankings
        ranks = {0,1,2,3} - {i}
        for num in ranks:
            counter += sprinters[num][2]
            team.append(sprinters[num][0])
    else:
        for j in range(3):
            counter += sprinters[j][2]
            team.append(sprinters[j][0])
    if counter < lowest_time:
        lowest_time = counter
        best_team = team

print(lowest_time)
print('\n'.join(best_team))
        
    


