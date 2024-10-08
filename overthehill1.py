from sys import stdin,stdout

mappings = {"A": 0, "B": 1, "C": 2, "D": 3,
            "E": 4, "F": 5, "G": 6, "H": 7,
            "I": 8, "J": 9, "K": 10, "L": 11,
            "M": 12, "N": 13, "O": 14, "P": 15,
            "Q": 16, "R": 17, "S": 18, "T": 19,
            "U": 20, "V": 21, "W": 22, "X": 23,
            "Y": 24, "Z": 25, "0": 26, "1": 27,
            "2": 28, "3": 29, "4": 30, "5": 31,
            "6": 32, "7": 33, "8": 34, "9": 35,
            " ": 36}
reverse_mappings = {v: k for k,v in mappings.items()}

# assume dimensions are compatible
def multiply(m1,m2):
    r1,c1,r2,c2 = len(m1),len(m1[0]),len(m2),len(m2[0])
    res = [[0 for i in range(c2)] for j in range(r1)]
    for i in range(r1):
        for j in range(c2):
            res[i][j] = sum(m1[i][k] * m2[k][j] for k in range(c1)) % 37
    return res

n = int(stdin.readline())
matrix = [list(map(int,stdin.readline().split())) for _ in range(n)]
plaintext = list(stdin.readline().strip())
L = len(plaintext)
for i in range((n - L % n) % n):
    plaintext.append(" ")
groups = [[[mappings[plaintext[j]]] for j in range(i,i + n)] for i in range(0,len(plaintext),n)]
encrypted_groups = [multiply(matrix, group) for group in groups]
result = []
for g in encrypted_groups:
    for row in g:
        for char in row:
            result.append(reverse_mappings[char])
stdout.write("".join(result))
