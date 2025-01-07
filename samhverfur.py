from sys import stdout

def findLargestPalindrome(n):
    num = str(n)
    # take first half digits and mirror them
    half = num[:len(num) // 2]
    # odd number of digits
    if len(num) % 2:
        res = half + num[(len(num) - 1) // 2] + half[::-1]
        if int(res) > n:
            d = int(num[(len(num) - 1) // 2])
            if d > 0:
                d -= 1
                new_res = half + str(d) + half[::-1]
                return new_res
            else:
                # subtract 1 from first half digits
                new_half = str(int(half) - 1)
                # edge case where number of digits change after decrementing by 1
                if len(new_half) == len(half) - 1:
                    new_res = new_half + "99" + new_half[::-1]
                else:
                    new_res = new_half + "9" + new_half[::-1]
                return new_res       
        else:
            return res
    else:
        res = half + half[::-1]
        if int(res) > n:
            # subtract 1 from first half digits
            new_half = str(int(half) - 1)
            # edge case where number of digits change after decrementing by 1
            if len(new_half) == len(half) - 1:
                new_res = new_half + "9" + new_half[::-1]
            else:
                new_res = new_half + new_half[::-1]
            return new_res
        else:
            return res

for i in range(1,101):
    stdout.write(f"{i} {findLargestPalindrome(pow(2,i))}\n")


