from itertools import permutations

# approach runs in O(N!) time
N,K = map(int,input().split())
positions = list(map(int,input().split()))
weights = list(map(int,input().split()))
perm = [i for i in range(N)]
ans = float("inf")
for order in permutations(perm):
    t,w,chosen = 0,0,[]
    # greedily take up as many tree saplings as possible going down the order
    for idx in order:
        t += 1
        if w + weights[idx] <= K:
            w += weights[idx]
            chosen.append(idx)
        else:
            max_pos = -1
            for j in chosen:
                if positions[j] > max_pos:
                    max_pos = positions[j]
            t += len(chosen) + max_pos * 2
            w = weights[idx]
            chosen = [idx]
    if chosen:
        max_pos = -1
        for j in chosen:
            if positions[j] > max_pos:
                max_pos = positions[j]
        t += len(chosen) + max_pos * 2
        w = weights[idx]
        chosen = [idx]
    ans = min(t,ans)
print(ans)
