from sys import stdin

def parse_time_string(ts, is_hour):
    ts = ts.split(",")
    times = []
    for s in ts:
        if "-" in s:
            s = s.split("-")
            for i in range(int(s[0]),int(s[1]) + 1):
                times.append(i)
        elif s == "*":
            end = 24 if is_hour else 60
            for i in range(end):
                times.append(i)
        else:
            times.append(int(s))
    return times

n = int(stdin.readline())
slots = [0 for _ in range(24 * 60 * 60)]
ans = 0
for i in range(n):
    h,m,s = stdin.readline().split()
    hours = parse_time_string(h, True)
    minutes = parse_time_string(m, False)
    seconds = parse_time_string(s, False)
    for a in hours:
        for b in minutes:
            for c in seconds:
                slots[a * 60 * 60 + b * 60 + c] += 1
    ans += len(hours) * len(minutes) * len(seconds)
job_starts = sum(slots[i] > 0 for i in range(len(slots)))
print(f"{job_starts} {ans}")
