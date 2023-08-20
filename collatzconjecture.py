from sys import stdin,stdout
from math import gcd

n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
# let st[i] contain the set of gcd of all possible subarrays from 0 to i inclusize
# maximum size of st[i] = log(arr[0]) + 1
# overall time complexity is O(n log^2 A), where A is maximum element in array
st = [set() for i in range(n)]
distinct = {arr[0]}
st[0].add(arr[0])
for i in range(1,n):
    for v in st[i - 1]:
        d = gcd(v,arr[i])
        st[i].add(d)
        distinct.add(d)
    st[i].add(arr[i])
    distinct.add(arr[i])
stdout.write(f"{len(distinct)}\n")
