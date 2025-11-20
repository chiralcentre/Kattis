c = int(input())
votes = sorted(map(int,input().split()))
total = sum(votes)
for i in range(c - 2):
    votes[-2] += votes[i]
    if (votes[-2] << 1) > total:
        print(i + 1)
        break
else:
    print("IMPOSSIBLE TO WIN")
