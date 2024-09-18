from sys import stdin,stdout

frame = "#."
M,N = map(int,stdin.readline().split())
U,L,R,D = map(int,stdin.readline().split())
words = [stdin.readline().strip() for _ in range(M)]
for i in range(U + M + D):
    if U <= i < U + M: # main puzzle
        for j in range(L):
            stdout.write(frame[j % 2]) if not i % 2 else stdout.write(frame[1 - j % 2])
        stdout.write(words[i - U])
        for j in range(R):
            stdout.write(frame[(j + L + N) % 2]) if not i % 2 else stdout.write(frame[1 - (j + L + N) % 2])
    else: # upper and lower frame
        for j in range(L + N + R):
            stdout.write(frame[j % 2]) if not i % 2 else stdout.write(frame[1 - j % 2])
    stdout.write("\n")
