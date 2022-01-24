n = int(input())
days = list(map(int,input().split()))
dirtypushes,cleanups = [],0

for j in range(1,366):
    switch = False #switch keeps track of whether the day happened to be a day where a dirty push was made
    if days and j == days[0]:
        dirtypushes.append(days.pop(0))
        switch = True
    dirtiness = sum(j-day for day in dirtypushes)
    if dirtiness >= 20 or (j == 365 and (dirtiness > 0 or dirtypushes)):
        dirtypushes = [dirtypushes[-1]] if switch else []
        cleanups += 1
    
print(cleanups)
        
        
