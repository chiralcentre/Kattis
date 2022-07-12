from sys import stdin,stdout

#If k = 0, we can solve the problem by doing the following:
#For each person, create two events, arrival and departure
#Sort all events, and sort arrivals before departures
#counter = 0
#for each event: if event is arrival, counter += 1, else counter -= 1
#keep track of maximum value of counter
#if k > 0, it is equivalent to staying for 0 seconds while everyone else stays for k seconds longer
n,k = map(int,stdin.readline().split())
events,counter,highest = [],0,0
for i in range(n):
    a,b = map(int,stdin.readline().split())
    events.append((a,'A')) 
    events.append((b+k,'D')) 
#sort by timing before sorting by arrival/departure in O(n log n) time
events.sort(key = lambda x: (x[0],x[1])) 
for t,e in events:
    counter += 1 if e == 'A' else -1
    if counter > highest:
        highest =  counter
stdout.write(str(highest))
