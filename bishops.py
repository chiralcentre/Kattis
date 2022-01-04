#Credit to Geeksforgeeks: The maximum bishops that can be placed on an n * n chessboard will be 2 * (n – 1) if n >= 2
#Place n bishops in first row
#Place n-2 bishops in last row. We only leave two corners of last row
import sys

def bishops(n):
    return 2*n - 2 if n >= 2 else 1 if n == 1 else 0

for line in sys.stdin:
    print(bishops(int(line)))
