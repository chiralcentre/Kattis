first = False
while True:
    n = int(input())
    if n == 0:
        break
    if not first:
        first = True
    else:
        print() #new line
    events = []
    for _ in range(n):
        time = input().split()
        hour,minutes = map(int,time[0].split(":"))
        if hour == 12:
            if time[1] == 'a.m.': hour -= 12
        elif time[1] == 'p.m.':
            hour += 12
        events.append((hour,minutes))       
    events = sorted(events)
    for H,M in events:
        if H == 0:
            print(f"12:{M} a.m.") if M >= 10 else print(f"12:0{M} a.m.")
        elif 0 < H < 12:
            print(f"{H}:{M} a.m.") if M >= 10 else print(f"{H}:0{M} a.m.")
        elif H == 12:
            print(f"{H}:{M} p.m.") if M >= 10 else print(f"{H}:0{M} p.m.")
        elif 12 < H < 24:
            print(f"{H-12}:{M} p.m.") if M >= 10 else print(f"{H-12}:0{M} p.m.")
    
    
