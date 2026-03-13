# Check the cells (2,2), (2,4) and (4,2) in order to see which square of 3 units does treasure chest lie in
# If there is no hit, the treasure chest must lie somewhere in the square centred (4,4)
cells = [(2,2),(2,4),(4,2)]
fx,fy = 4,4
for x,y in cells:
    print(f"? {x} {y}")
    res = int(input())
    if res == 1:
        fx,fy = x,y
        break
# Assume there is a hit for a centre (x,y)
# 1. Check if there is a hit for (x + 1, y). If yes, go to 1a, else go to 1b
# 1a. Check if there is a hit for (x, y - 1). If yes, print (x, y - 1), else print (x,y)
# 1b. Check if there is a hit for (x - 1, y - 1). If yes, print (x - 1, y - 1) else print (x - 1, y)
print(f"? {fx + 1} {fy}")
if int(input()) == 1:
    print(f"? {fx} {fy - 1}")
    if int(input()) == 1:
        print(f"! {fx} {fy - 1}")
    else:
        print(f"! {fx} {fy}")
else:
    print(f"? {fx - 1} {fy - 1}")
    if int(input()) == 1:
        print(f"! {fx - 1} {fy - 1}")
    else:
        print(f"! {fx - 1} {fy}")
