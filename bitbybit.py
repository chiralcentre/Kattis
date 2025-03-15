from sys import stdin,stdout

def get_pos(a):
    return 31 - a

mappings = ["0","1","?"]
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    register = [2 for i in range(32)]
    for i in range(n):
        seq = stdin.readline().strip().split()
        a = int(seq[1])
        if seq[0] == "CLEAR":
            register[get_pos(a)] = 0
        elif seq[0] == "SET":
            register[get_pos(a)] = 1
        elif seq[0] == "OR":
            u,v = get_pos(a),get_pos(int(seq[2]))
            if register[u] == 1 or register[v] == 1:
                register[u] = 1
            elif register[u] == 0 and register[v] == 0:
                register[u] = 0
            else:
                register[u] = 2
        else: # and command
            u,v = get_pos(a),get_pos(int(seq[2]))
            if register[u] == 1 and register[v] == 1:
                register[u] = 1
            elif register[u] == 0 or register[v] == 0:
                register[u] = 0
            else:
                register[u] = 2
    stdout.write("".join(mappings[bit] for bit in register))
    stdout.write("\n")
