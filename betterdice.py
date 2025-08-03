from sys import stdin
from bisect import bisect_right

# code runs in O(n log n)
n = int(stdin.readline())
first = sorted(map(int,stdin.readline().split()))
second = sorted(map(int,stdin.readline().split()))
first_numerator,second_numerator = 0,0
# for every number on first die, find numbers on second die larger
for x in first:
    index = bisect_right(second,x)
    second_numerator += n - index
# for every number on second die, find numbers on first die larger
for x in second:
    index = bisect_right(first,x)
    first_numerator += n - index
if first_numerator > second_numerator:
    print("first")
elif first_numerator < second_numerator:
    print("second")
else:
    print("tie")
   
