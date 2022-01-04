n,valid_scores = int(input()),list(filter(lambda x: x >= 0, map(int, input().split())))
print(sum(valid_scores)/len(valid_scores))
