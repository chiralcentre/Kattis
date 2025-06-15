x1,y1,x2,y2 = map(int,input().split())
corners = {(0,0), (0, 2024), (2024, 0), (2024, 2024)}
ans = 0
if (x1,y1) not in corners:
    ans += 1
if (x2,y2) not in corners:
    ans += 1
print(ans)