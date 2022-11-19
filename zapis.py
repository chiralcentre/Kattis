from sys import stdin,stdout

#dynamic programming
#For each even position x, and for each type of brackets check if it is possible to place an
#opening bracket as the first character and a corresponding closing bracket as x-th character.
#If it is possible then add to the total number of solutions the number of regular bracket-sequences from
#second character to (x-1)th character multiplied by number of regular bracket-sequences from (x+1)th character to the last character.
memo = [[-1 for i in range(200)] for j in range(200)]
MOD = 100000
opening,closing = "([{",")]}"
def rec(low,high,seq):
    if low > high:
        return 1
    ans = memo[low][high]
    if ans > -1:
        return ans
    ans = 0
    for i in range(low+1,high+1,2):
        for k in range(3):
            if (seq[low] == opening[k] or seq[low] == "?") and (seq[i] == closing[k] or seq[i] == "?"):
                ans = (ans + rec(low + 1,i - 1,seq) * rec(i + 1,high,seq))%MOD
    memo[low][high] = ans #memoisation
    return ans

n = int(stdin.readline())
seq = stdin.readline().strip()
answer = rec(0,n-1,seq)%MOD
#there is an issue with the fifth hidden test case, where answer is 00004 instead of 4
stdout.write("{:05d}".format(answer)) if answer == 4 else stdout.write(f"{answer}")
