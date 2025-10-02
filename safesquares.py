grid = [input().strip() for _ in range(8)]
rows,columns = set(),set()
for i in range(8):
    for j in range(8):
        if grid[i][j] == "R":
            rows.add(i)
            columns.add(j)
print((8 - len(rows)) * (8 - len(columns)))
