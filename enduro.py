from sys import stdin,stdout

SIX_PM = 18 * 3600
NOON = 12 * 3600
DAY = 24 * 3600

def parse_time(time_string, indicator):
    h,m,s = map(int,time_string.split(":"))
    if indicator == "AM" and h == 12:
        h = 0
    if indicator == "PM" and h != 12:
        h += 12
    return h * 3600 + m * 60 + s

first_line = stdin.readline().split()
st = parse_time(first_line[0], first_line[1])
et = st + 10800 # 3 hours later from start time
laps,last_seen,finished = {},{},set()
for i in range(int(stdin.readline())):
    time_string,indicator,name = stdin.readline().strip().split(" ", 2)
    if name not in finished:
        time = parse_time(time_string,indicator)
        if st >= SIX_PM and time < NOON:
            time += DAY
        last_seen[name] = time
        laps[name] = laps.get(name,0) + 1
        if time >= et:
            finished.add(name)
             
pairs = []
for key in laps:
    if last_seen[key] >= et:
        pairs.append((laps[key],last_seen[key],key))
# descending order of laps completed, ascending order of finish time
pairs.sort(key = lambda x: (-x[0],x[1]))
for num,_,name in pairs:
    stdout.write(f"{num} {name}\n")
