from sys import stdin,stdout

MOD = 1000000007
for _ in range(int(stdin.readline())):
    d = int(stdin.readline())
    #there are only 8 choices for first digit, since 0 cannot be first digit
    stdout.write(f"{(8 * pow(9,d - 1,MOD)) % MOD}\n")
