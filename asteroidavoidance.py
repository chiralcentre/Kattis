from sys import stdin,stdout

def solve(xr,yr,w,h,asteroids):
    corners = [(xr,yr),(xr+w,yr),(xr,yr+h),(xr+w,yr+h)]
    # circle intersects with rectangle if any of three cases is true
    # 1. centre of asteroid is inside rectangle
    # 2. centre of asteroid is less than radius of asteroid from sides of rectangle
    # 3. centre of asteroid is less than radius of asteroid from corners of rectangle
    for xa,ya,ra in asteroids:
        if (xr <= xa <= xr + w and yr <= ya <= yr + h) or (xr <= xa <= xr + w and yr - ra <= ya <= yr + ra + h) or (yr <= ya <= yr + h and xr - ra <= xa <= xr + w + ra):
            return "STOP!"
        for a,b in corners:
            if pow(a - xa, 2) + pow(b - ya, 2) <= pow(ra, 2):
                return "STOP!"
    return "GO!"

w,h = map(int,stdin.readline().split())
n,m = map(int,stdin.readline().split())
asteroids = [tuple(map(int,stdin.readline().split())) for _ in range(n)]
for i in range(m):
    xr,yr = map(int,stdin.readline().split())
    stdout.write(f"DOOMSLUG {solve(xr,yr,w,h,asteroids)}\n")
