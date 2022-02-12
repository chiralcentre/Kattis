probabilities = sorted([float(input().split()[1]) for _ in range(int(input()))],reverse = True)
print(sum(probabilities[i]*(i+1) for i in range(len(probabilities))))
