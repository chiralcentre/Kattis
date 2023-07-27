from sys import stdin,stdout
from bisect import bisect_left

'''
Given is an ordered list of items, and every item has a list of
numbers (i.e. the stores where they can be bought).
Can we choose a single number in this list for every item such
that the list is non-decreasing. Also, can this be done
uniquely?
The first question is relatively easy: starting from the front,
greedily adhere the lowest number to each item that is at
least the previous number.
To determine whether it is unique, there is an elegant solution:
repeat the process, but start from the rear, and greedily
choose the highest number. If you get the same path as in the
previous step, the answer is unique, otherwise ambiguous
'''

def solve():
    N,K = int(stdin.readline()),int(stdin.readline())
    items,negItems,shopping = {},{},[]
    for _ in range(K):
        i,S = stdin.readline().split()
        i = int(i)
        if S not in items:
            items[S] = [i]
            negItems[S]= [-i]
        else:
            items[S].append(i)
            negItems[S].append(-i)
    # sort store numbers
    for k in items:
        items[k].sort()
        negItems[k].sort()
    M = int(stdin.readline())
    for _ in range(M):
        shopping.append(stdin.readline().strip())
    if M == 0:
        return "ambiguous"
    # Starting from first item in shopping list, greedily choose lowest store number for each item that is at least the previous number
    # every item is available at least one store, so checking for empty stores is not required
    firstSol = [items[shopping[0]][0]]
    for i in range(1,M):
        index = bisect_left(items[shopping[i]],firstSol[-1])
        if index >= len(items[shopping[i]]) or items[shopping[i]][index] < firstSol[-1]:
            return "impossible"
        else:
            firstSol.append(items[shopping[i]][index])
    # repeat process starting from the last item in shopping list and greedily choose highest number less than or equal to previous number
    secondSol = [-negItems[shopping[-1]][0]]
    for i in range(M - 2, -1, -1):
        index = bisect_left(negItems[shopping[i]],-secondSol[-1])
        if index >= len(negItems[shopping[i]]) or negItems[shopping[i]][index] < -secondSol[-1]:
            return "impossible"
        else:
            secondSol.append(-negItems[shopping[i]][index])
    secondSol.reverse()
    return "unique" if firstSol == secondSol else "ambiguous"

stdout.write(solve())
