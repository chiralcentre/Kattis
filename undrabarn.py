# convert to base 8 with digits [1,2,3,4,5,6,7,9]
# time complexity: log(K)
digits = [1,2,3,4,5,6,7,9]
K = int(input())
final = []
while K > 0:
    R = K % 8
    if R == 0:
        final.append(str(digits[-1]))
        K = K // 8 - 1
    else:
        final.append(str(digits[R - 1]))
        K //= 8
print("".join(final[::-1]))
