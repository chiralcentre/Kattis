def squared_euclidean_distance(p1,p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def cross_product(v1,v2):
    x1,y1 = v1; x2,y2 = v2
    return x1 * y2 - x2 * y1

def vector(p1,p2):
    return (p2[0] - p1[0],p2[1] - p1[1])

def solve():
    p1,p2,p3,p4 = [tuple(map(int,input().split())) for i in range(4)]
    s1,s2 = squared_euclidean_distance(p1,p2),squared_euclidean_distance(p2,p3)
    s3,s4 = squared_euclidean_distance(p3,p4),squared_euclidean_distance(p4,p1)
    d1,d2 = squared_euclidean_distance(p1,p3),squared_euclidean_distance(p2,p4)
    # if all sides are equal and both diagonals are equal, shape is square
    # if all sides are equal and both diagonals are not equal, shape is rhombus
    if s1 == s2 == s3 == s4:
        return "square" if d1 == d2 else "rhombus"
    # if opposing sides are equal and both diagonals are equal, shape is rectangle
    # if opposing sides are equal and both diagonals are not equal, shape is parallelogram
    if s1 == s3 and s2 == s4:
        return "rectangle" if d1 == d2 else "parallelogram"
    # if two pairs of adjacent sides are equal, shape is kite
    if (s1 == s2 and s3 == s4) or (s2 == s3 and s4 == s1):
        return "kite"
    # if two opposing sides are parallel, shape is trapezium
    # check cross product of vectors = 0 -> parallel
    if 0 in [cross_product(vector(p1,p2),vector(p3,p4)),cross_product(vector(p1,p3),vector(p2,p4)), cross_product(vector(p2,p3),vector(p1,p4))]:
        return "trapezium"
    return "none"
    
if __name__ == "__main__":
    print(solve())
