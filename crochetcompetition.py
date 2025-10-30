mappings = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3,
            "Fri": 4, "Sat": 5, "Sun": 6}

HOUR = 60
DAY = 24 * HOUR
WEEK = 7 * DAY
first_line = input().split()
fh,fm = map(int,first_line[1].split(":"))
first_time = mappings[first_line[0]] * DAY + fh * HOUR + fm
second_line = input().split()
sh,sm = map(int,second_line[1].split(":"))
second_time = mappings[second_line[0]] * DAY + sh * HOUR + sm

diff = second_time - first_time
if diff <= 0:
    diff +=  WEEK
ans = []
days = diff // DAY
if days == 1:
    ans.append("1 day")
elif days > 1:
    ans.append(f"{days} days")
diff %= DAY
hours = diff // HOUR
if hours == 1:
    ans.append("1 hour")
elif hours > 1:
    ans.append(f"{hours} hours")
diff %= HOUR
mins = diff
if mins == 1:
    ans.append("1 minute")
elif mins > 1:
    ans.append(f"{mins} minutes")

if len(ans) == 1:
    print(ans[0])
elif len(ans) == 2:
    print(" and ".join(ans))
else:
    print(", ".join(ans))

