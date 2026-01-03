from sys import stdin

N = int(stdin.readline())
mappings = {"Sunday": 0, "Monday": 1, "Tuesday": 2,
            "Wednesday": 3, "Thursday": 4, "Friday": 5,
            "Saturday": 6}
reverse_mappings = {v: k for k,v in mappings.items()}
office_hours = [0 for _ in range(24 * 7)]
for i in range(N):
    _,d,_,*hours = stdin.readline().split()
    d = mappings[d]
    for h in hours:
        office_hours[d * 24 + int(h)] += 1
best,ans = -1,-1
for i in range(len(office_hours)):
    if office_hours[i] > best:
        best,ans = office_hours[i],i
D = reverse_mappings[ans // 24]
T = str(ans % 24).zfill(2)
print(f"Your professor should host office hours {D} @ {T}:00")
