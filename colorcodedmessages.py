from sys import stdin

colours = {
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "aqua": (0, 255, 255),
    "fuchsia": (255, 0, 255),
    "silver": (192, 192, 192),
    "maroon": (128, 0, 0),
    "orange": (255, 165, 0),
    "indigo": (75, 0, 130),
    "emerald": (80, 200, 120),
    "ultramarine": (18, 10, 143),
    "hazel": (165, 42, 42),
    "pink": (255, 192, 203),
    "crimson": (220, 20, 60),
}

ans = []
for _ in range(int(stdin.readline())):
    pixels = tuple(map(int,stdin.readline().split()))
    if pixels[0] == pixels[1] == pixels[2] == 0:
        ans.append(" ")
        continue
    closest,best_err = None,25
    for k,v in colours.items():
        err = sum(abs(pixels[i] - v[i]) for i in range(len(pixels)))
        # only one colour is the closest
        if err < best_err:
            closest,best_err = k,err
    ans.append(closest[0])
print("".join(ans))
        
    
