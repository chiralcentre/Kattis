def reverse_binary(num):
    binary_reverse = []
    while num > 0:
        remainder = num%2
        binary_reverse.append(remainder)
        num //= 2
    return binary_reverse

N = int(input())
new_num = reverse_binary(N)
print(sum(new_num[i]*2**(len(new_num)-1-i) for i in range(len(new_num))))
