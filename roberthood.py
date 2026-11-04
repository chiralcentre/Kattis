from sys import stdin
from math import sqrt

# code runs in O(n + M^2) time
def max_euclidean_distance(points):
    # Filter points using the small coordinate constraint (-1000 <= x, y <= 1000)
    # Map each x to its min and max y found so far
    min_y_for_x = {}
    max_y_for_x = {}
    for x,y in points:
        if x not in min_y_for_x or y < min_y_for_x[x]:
            min_y_for_x[x] = y
        if x not in max_y_for_x or y > max_y_for_x[x]:
            max_y_for_x[x] = y
    # Collect all extreme boundary points
    candidates = set()
    for x in min_y_for_x:
        candidates.add((x, min_y_for_x[x]))
        candidates.add((x, max_y_for_x[x]))
        
    candidate_list = list(candidates)
    M = len(candidate_list)
    # Compare pairs among the drastically reduced candidate set
    # M is at most 2 * 2001 = 4002
    max_sq_dist = 0
    for i in range(M):
        x1,y1 = candidate_list[i]
        for j in range(i + 1, M):
            x2,y2 = candidate_list[j]
            sq_dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
            if sq_dist > max_sq_dist:
                max_sq_dist = sq_dist        
    return sqrt(max_sq_dist)

C = int(stdin.readline())
points = [tuple(map(int,stdin.readline().split())) for _ in range(C)]
print(max_euclidean_distance(points))
