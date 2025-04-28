from sys import stdin,stdout

moves = [1,2,3,4,5,
         6,7,8,9,10,
         11,12,13,14,15,
         16,17,18,19,20,
         25,50]
string_mappings = {25: "Outer bullseye", 50: "Bullseye",
                   1: "Single", 2: "Double", 3: "Triple"
                   }

visited = [[] for _ in range(502)]
frontier = [([],0)]
for i in range(3):
    temp_frontier = []
    for curr_lst,total in frontier:
        for m3 in moves:
            if m3 == 25 or m3 == 50:
                temp = curr_lst + [string_mappings[m3]]
                temp_frontier.append((temp, total + m3))
                visited[total + m3].append(temp)
            else:
                for j in range(1,4):
                    temp = curr_lst + [f"{string_mappings[j]} {m3}"]
                    temp_frontier.append((temp, total + j * m3))
                    visited[total + j * m3].append(temp)
    frontier = temp_frontier

n = int(stdin.readline())
stdout.write(f"{len(visited[n])}\n")
for lst in visited[n]:
    stdout.write(f"{len(lst)}\n")
    for move in lst:
        stdout.write(f"{move}\n")
