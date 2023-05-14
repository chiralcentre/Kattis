from sys import stdin,stdout

bases = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
         "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12,
         "d": 13, "e": 14, "f": 15, "g": 16, "h": 17, "i": 18,
         "j": 19, "k": 20, "l": 21, "m": 22, "n": 23, "o": 24,
         "p": 25, "q": 26, "r": 27, "s": 28, "t": 29, "u": 30,
         "v": 31, "w": 32, "x": 33, "y": 34, "z": 35}

reverseBase = {v: k for k,v in bases.items()}
bases["0"] = 0; reverseBase[36] = "0"

for _ in range(int(stdin.readline())):
    X,op,Y,e,Z = stdin.readline().split()
    L,hasZero = 1,False
    for char in X:
        L = max(L,bases[char])
        if char == "0":
            hasZero = True
    for char in Y:
        L = max(L,bases[char])
        if char == "0":
            hasZero = True
    for char in Z:
        L = max(L,bases[char])
        if char == "0":
            hasZero = True
    ans = []
    #deal with special case of unary operator
    if L != 1 or (L == 1 and hasZero):
        L += 1
    for i in range(L,37):
        a = sum(bases[X[j]] * pow(i,len(X) - j - 1) for j in range(len(X)))
        b = sum(bases[Y[j]] * pow(i,len(Y) - j - 1) for j in range(len(Y)))
        c = sum(bases[Z[j]] * pow(i,len(Z) - j - 1) for j in range(len(Z)))
        if op == "+":
            if a + b == c:
                ans.append(reverseBase[i])
        elif op == "-":
            if a - b == c:
                ans.append(reverseBase[i])
        elif op == "*":
            if a * b == c:
                ans.append(reverseBase[i])
        else: # divide operator
            if not a % b and a // b == c:
                ans.append(reverseBase[i])
    stdout.write("".join(b for b in ans)) if ans else stdout.write("invalid")
    stdout.write("\n")
