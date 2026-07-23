from sys import stdin

N,x,y = map(int,stdin.readline().split())
# maximum reach occurs when all segments are pointing in the same direction (sum all segments)
# minimum reach = max(0, 2 * M - T), where M is length of largest segment and T is sum of all segments
# proof: let vector v_1 be the segment with length M. All other vectors sum up to vector u.
# by triangle inequality, |u| = |v_2 + v_3 + ... + v_N} <= |v_2| + |v_3| + ... + |v_N| = T - M
# by reverse triangle inequality, |v_1 + u| >= |v_1| - |u| >= |v_1| - (T - M) = 2 * M - T
B,T = 0,0
for _ in range(N):
    s = int(stdin.readline())
    T += s
    B = max(s,B)
L = max(0,2 * B - T)
H = T
D = x ** 2 + y ** 2
print("YES") if L * L <= D <= H * H else print("NO")
    
