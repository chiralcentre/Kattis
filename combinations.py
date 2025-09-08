def convert_to_digits(num):
    s = str(num).zfill(4)
    return list(map(int,list(s)))

def solve():
    INF = pow(10,9)
    first,second = int(input()),int(input())
    visited,frontier = [INF for i in range(10000)],[first]
    visited[first] = 0
    # perform BFS in O(V + E) time
    # V = 10000, E = 20 edges per vertex
    while frontier:
        new_frontier = []
        for num in frontier:
            curr = visited[num]
            digits = convert_to_digits(num)
            for i in range(len(digits)):
                for j in range(i, len(digits)):
                    # forwards
                    temp = [d for d in digits]
                    for k in range(i,j + 1):
                        temp[k] = (temp[k] + 1) % 10
                    new_num = sum(temp[index] * pow(10, len(temp) - index - 1) for index in range(len(temp)))
                    if curr + 1 < visited[new_num]:
                        visited[new_num] = curr + 1
                        new_frontier.append(new_num)
                    if new_num == second:
                        return visited[new_num]
                    # backwards
                    temp = [d for d in digits]
                    for k in range(i,j + 1):
                        temp[k] = (temp[k] - 1) % 10
                    new_num = sum(temp[index] * pow(10, len(temp) - index - 1) for index in range(len(temp)))
                    if curr + 1 < visited[new_num]:
                        visited[new_num] = curr + 1
                        new_frontier.append(new_num)
                    if new_num == second:
                        return visited[new_num]
        frontier = new_frontier
    raise Exception("not supposed to reach here")

print(solve())
