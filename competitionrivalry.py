from sys import stdin

def get_penalty_and_ts(subs,scores):
    total_penalty,latest_timestamp = 0,0
    for key,lst in subs.items():
        # ignore problems with non positive score
        if scores[key] == 0:
            continue
        # find timestamp of earliest submission with best score in O(L) time, where L is size of list
        best,earliest = -1,None
        for s,t in lst:
            if s > best:
                best,earliest = s,t
            elif s == best and t < earliest:
                earliest = t
        latest_timestamp = max(latest_timestamp,earliest)
        # find number of submissions earlier than earliest submission with best score in O(L) time
        penalty = earliest
        for s,t in lst:
            if t < earliest:
                penalty += 20
        total_penalty += penalty
    return total_penalty,latest_timestamp

# return results for first and third rule
def first_third_rule(e_subs,e_scores,r_subs,r_scores):
    ep,et = get_penalty_and_ts(e_subs,e_scores)
    rp,rt = get_penalty_and_ts(r_subs,r_scores)
    return "YES" if ep < rp else "NO", "YES" if et < rt else "NO"

# overall code runs in O(x + y) time 
n,x = int(stdin.readline()),int(stdin.readline())
e_subs,e_scores = {},{}
for _ in range(x):
    p,s,t = map(int,stdin.readline().split())
    if p not in e_subs:
        e_subs[p] = [(s,t)]
    else:
        e_subs[p].append((s,t))
    e_scores[p] = max(e_scores.get(p,0),s)
y = int(stdin.readline())
r_subs,r_scores = {},{}
for _ in range(y):
    p,s,t = map(int,stdin.readline().split())
    if p not in r_subs:
        r_subs[p] = [(s,t)]
    else:
        r_subs[p].append((s,t))
    r_scores[p] = max(r_scores.get(p,0),s)
E,R = sum(e_scores.values()),sum(r_scores.values())
if E > R:
    print("YES YES YES")
elif E < R:
    print("NO NO NO")
else: # equality case, tiebreak
    first,third = first_third_rule(e_subs,e_scores,r_subs,r_scores)
    second = "YES" if x < y else "NO"
    print(f"{first} {second} {third}")
