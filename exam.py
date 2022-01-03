k = int(input())
answer1,answer2 = input().strip(),input().strip()
overlap = [answer1[i] for i in range(len(answer1)) if answer1[i] == answer2[i]]
print(len(answer1) - k + len(overlap)) if k >= len(overlap) else print(len(answer1)+ k - len(overlap))
