from sys import stdin

# Sort the animals in decreasing order of strength
# Maintain the current stable set of animals, which starts with just the strongest animal
# Looping over the other animals in decreasing order, maintain a candidate set of animals.
# The moment that the candidate set of animals has sum of strengths greater than or equal to the current stable set,
# merge that set into the stable set and reset the candidate set.
# The answer is the final size of the stable set.
# Animals are only willing to eliminate other animals if they themselves will not be eliminated
n = int(stdin.readline())
# sort in descending order
strengths = sorted([int(stdin.readline()) for _ in range(n)],reverse = True)
# the strongest animal is guaranteed to stay
remain,remain_total,running_total,running_num = 1,strengths[0],0,0
for i in range(1,n):
    running_total += strengths[i]
    running_num += 1
    if running_total >= remain_total:
        remain_total += running_total
        remain += running_num
        running_total,running_num = 0,0
print(remain)
