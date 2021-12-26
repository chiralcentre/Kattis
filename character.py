N = int(input())
# if a set has n elements, it has 2**n - 1 subsets, excluding the empty set, and N subsets with one member
print(2**N - N - 1)
