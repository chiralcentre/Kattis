d = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
f,s = input().strip(),input().strip()
fc,sc = d.index(f),d.index(s)
if fc == sc:
    print("Keep going straight")
elif abs(fc - sc) == 4:
    print("U-turn")
elif fc < sc:
    a = (sc - fc) * 45
    m = "starboard"
    if a > 180:
        m,a = "port",360 - a
    print(f"Turn {a} degrees {m}")
else:
    a = (fc - sc) * 45
    m = "port"
    if a > 180:
        m,a = "starboard",360 - a
    print(f"Turn {a} degrees {m}")
