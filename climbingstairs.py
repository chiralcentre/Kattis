#We can always postpone registering to last possible moment
#We can go to office first, register at end of day, and go home
#If there are insufficient steps when we reach the registration office, increment the number of steps by 2 (upwards and downwards) until it is enough.

n,r,k = map(int,input().split())
#number of steps taken to reach registration office is k + abs(r - k) since registration office can be below or above office
#if k + abs(r - k) < n, increment steps by 2 until number of steps >= n.
#number of steps taken to get down from registration offfice = r
print(max(n,k + abs(r-k)) + r + (1 if n%2 != r%2 and n > k + abs(k - r) else 0))
