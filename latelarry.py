line = input().split()
T = int(input())
h,m = map(int,line[0].split(":"))
t = h * 60 + m if h != 12 else m
if line[1] == "PM":
    t += 720
t = (t - T) % 1440
H,M = t // 60,t % 60
D = "PM" if H >= 12 else "AM"
if H == 0:
    H = 12
elif H >= 13:
    H %= 12
print(f"{H}:{str(M).zfill(2)} {D}")
