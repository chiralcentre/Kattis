from math import ceil
s,t,n = map(int,input().split())
walk_times = list(map(int,input().split()))
bus_times = list(map(int,input().split()))
intervals = list(map(int,input().split()))
s += walk_times[0]
for i in range(n):
    s = max(s,intervals[i]*ceil(s/intervals[i]))
    s += bus_times[i] + walk_times[i+1]
print('yes') if s <= t else print('no')
