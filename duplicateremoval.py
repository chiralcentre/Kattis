from sys import stdin,stdout

for line in stdin:
    N,*guesses = line.split()
    if N == "0":
        break
    output = [guesses[0]]
    for i in range(1,int(N)):
        if guesses[i] != guesses[i - 1]:
            output.append(guesses[i])
    output.append("$")
    stdout.write(" ".join(output))
    stdout.write("\n")
