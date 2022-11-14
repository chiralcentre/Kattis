from sys import stdin,stdout

#Number of bell tolls required for x zebras below = 2**x
stdout.write(str((lambda N: sum(2**(N - i - 1) for i in range(N) if stdin.readline().strip() == "O"))(int(stdin.readline()))))
