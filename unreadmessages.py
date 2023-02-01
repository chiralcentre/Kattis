from sys import stdin,stdout

n,m = map(int,stdin.readline().split())
#senders[i] contains list of timings messages were sent for i
senders,total = {},0
#O(m)
for i in range(m):
    s = int(stdin.readline())
    #increment of n - 1 at every step
    total += n - 1
    total -= i - senders[s][-1] - 1 if s in senders else i
    if s in senders:
        senders[s].append(i)
    else:
        senders[s] = [i]
    stdout.write(f"{total}\n")
