# function returns sum of terms starting from s with step d up to end
def arithmetic_sum(s,d,end):
    n = (end - s) // d + 1
    return (n * (2 * s + (n - 1) * d)) >> 1

p = int(input())
# principle of inclusion/exclusion
print(arithmetic_sum(3,3,p - 1) + arithmetic_sum(5,5,p - 1) - arithmetic_sum(15,15,p - 1))
