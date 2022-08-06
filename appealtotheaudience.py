from sys import stdin,stdout

#intuitively, the number of games each team plays must be directly proportional to its skill level
#The best team must play the most games
n,k = map(int,stdin.readline().split())
#sort skill levels of players in O(k log k)
skills = sorted(map(int,stdin.readline().split()))
#p[a] stores the parent node of node a
p = [-1]
for i in range(n-1):
    p.append(int(stdin.readline()))
longest_path_length = [0 for _ in range(n)]
longest_path = []
#go from n - 1 to 1 in reverse
for i in range(n-1,0,-1):
    longest_path_length[i] += 1
    if longest_path_length[p[i]] > 0:
        longest_path.append(min(longest_path_length[i],longest_path_length[p[i]]))
    #update longest path length for parent node
    longest_path_length[p[i]] = max(longest_path_length[i],longest_path_length[p[i]])
longest_path.append(longest_path_length[0])
longest_path.sort() #O(n log n)
#match skill levels to path lengths
stdout.write(str(sum(skills[i]*longest_path[i] for i in range(k))))
