from sys import stdin

n = int(stdin.readline())
# sort in ascending order of house number
students = sorted([tuple(map(int,stdin.readline().split())) for _ in range(n)])
# output represents total carbon emitted assuming first house is taken
# total_carbon represents the sum of all the carbon rates
output,total_carbon = 0,0
for i in range(n):
    output += (students[i][0] - students[0][0]) * students[i][1]
    total_carbon += students[i][1]

best_output,ans,cum_carbon = output,students[0][0],students[0][1]
for i in range(1,n):
    output += (students[i][0] - students[i - 1][0]) * cum_carbon
    output -= (students[i][0] - students[i - 1][0]) * (total_carbon - cum_carbon)
    cum_carbon += students[i][1]
    if output < best_output:
        output,ans = best_output,students[i][0]
print(ans)
