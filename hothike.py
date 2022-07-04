from sys import stdin,stdout

#question can be interpreted as checking every contiguous subsequence of length 3 to minimise maximum temperature attained on first and last day

n = int(stdin.readline())
temperatures = list(map(int,stdin.readline().split()))
d,t = 0,999 #set temp as 999 since maximum temperature is 40
for i in range(n-2): #O(n)
    if max(temperatures[i],temperatures[i+2]) < t:
        d = i+1
        t = max(temperatures[i],temperatures[i+2])
stdout.write(f"{d} {t}")
