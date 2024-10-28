def get_prob(d1,d2):
    wins,same,loss = 0,0,0
    for i in range(len(d1)):
        for j in range(len(d2)):
            if d1[i] > d2[j]:
                wins += 1
            elif d1[i] == d2[j]:
                same += 1
            else:
                loss += 1
    total = len(d1) * len(d2) - same
    return (wins / total, loss / total) if total > 0 else (0,0)

def solve(d1,d2,d3):
    # probs[0] = probability of die 1 winning/losing die 2
    # probs[1] = probability of die 1 winning/losing die 3
    # probs[2] = probability of die 2 winning/losing die 3
    probs = [get_prob(d1,d2),get_prob(d1,d3),get_prob(d2,d3)]
    # check if die 1 can win
    if min(probs[0][0], probs[1][0]) >= 0.5:
        return "1"
    # check if die 2 can win
    if min(probs[0][1],probs[2][0]) >= 0.5:
        return "2"
    # check if die 3 can win
    if min(probs[1][1],probs[2][1]) >= 0.5:
        return "3"
    return "No dice"
        
d1 = list(map(int,input().split()))
d2 = list(map(int,input().split()))
d3 = list(map(int,input().split()))
print(solve(d1,d2,d3))
