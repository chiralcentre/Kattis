from sys import stdin,stdout

n = int(stdin.readline())
individual_scores = [int(stdin.readline()) for _ in range(n)]
current_score = sum(individual_scores[i]*(4/5)**i for i in range(n))/5
total = 0
for i in range(n):
    for j in range(n):
        if j < i:
            total += individual_scores[j]*(4/5)**j
        elif j > i:
            total += individual_scores[j]*(4/5)**(j-1)
total /= 5
stdout.write(f"{current_score}\n")
stdout.write(f"{total/n}\n")
