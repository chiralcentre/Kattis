from sys import stdin,stdout
from math import log,ceil

# product of every prime < 2^63
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
fact = [1,1]
for i in range(2,63):
    fact.append(fact[-1] * i)

# generate all possible numbers k of the form p_1^e_1 * p_2^e_2 * p_3^e_3..., where e_1 >= e_2 >= e_3 .... and p_i is the ith prime
# limit k < 2^63
# there are 43606 such numbers
nums,LIMIT = [],pow(2,63)
def recursive_gen(exponents,num,index):
    if index != len(primes) and num < LIMIT:
        if num > 1:
            nums.append((tuple(exponents), num))
        lb,ub = 1,ceil(log(LIMIT/num)/log(primes[index]))
        curr = num
        for i in range(lb,ub + 1):
            if index > 0 and i > exponents[index - 1]:
                break
            exponents[index] += 1
            curr *= primes[index]
            recursive_gen([x for x in exponents], curr, index + 1)

recursive_gen([0 for _ in range(len(primes))],1,0)

def find_total(arr):
    total,nonzero = 0,[]
    for elem in arr:
        if elem > 0:
            total += elem
            nonzero.append(elem)
    return total,nonzero

# compute f(k) for every k
memo = {}
for tup,v in nums:
    total,nonzero = find_total(tup)
    ans = fact[total]
    for elem in nonzero:
        ans //= fact[elem]
    memo[ans] = v if ans not in memo else min(memo[ans],v)

for line in stdin:
    n = int(line)
    stdout.write(f"{n} {memo[n]}\n")
