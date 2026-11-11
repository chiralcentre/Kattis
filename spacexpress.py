from sys import stdin,stdout

# assume both matrices are square and of the same dimensions
def is_similar(adj_1,adj_2):
    for i in range(len(adj_1)):
        for j in range(len(adj_1)):
            if i != j and adj_1[i][j] != adj_2[i][j]:
                return "NO"
    return "YES"

# assume character is uppercase
def get_idx(char):
    return ord(char) - ord("A")

output = []
for _ in range(int(stdin.readline())):
    stdin.readline() # read in blank line
    m1 = int(stdin.readline())
    adj_spcx = [[False for i in range(26)] for j in range(26)]
    for i in range(m1):
        a,b = stdin.readline().split()
        u,v = get_idx(a),get_idx(b)
        adj_spcx[u][v] = adj_spcx[v][u] = True
    for k in range(len(adj_spcx)):
        for i in range(len(adj_spcx)):
            for j in range(len(adj_spcx)):
                if adj_spcx[i][k] and adj_spcx[k][j]:
                    adj_spcx[i][j] = True
    m2 = int(stdin.readline())
    adj_comp = [[False for i in range(26)] for j in range(26)]
    for i in range(m2):
        a,b = stdin.readline().split()
        u,v = get_idx(a),get_idx(b)
        adj_comp[u][v] = adj_comp[v][u] = True
    for k in range(len(adj_comp)):
        for i in range(len(adj_comp)):
            for j in range(len(adj_comp)):
                if adj_comp[i][k] and adj_comp[k][j]:
                    adj_comp[i][j] = True
    output.append(f"{is_similar(adj_spcx,adj_comp)}\n\n")
stdout.write("".join(output))
