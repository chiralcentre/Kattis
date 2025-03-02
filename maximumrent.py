a,b = map(int,input().split())
m,s = map(int,input().split())
min_x, max_x = s - m, m - 1
min_y, max_y = 1, 2 * m - s
if min_x < 1 or max_y > m - 1:
    min_x = 1
    max_y = m - 1

ans1 = min_x * a + max_y * b
ans2 = max_x * a + min_y * b
print(max(ans1,ans2))
    
