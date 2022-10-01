from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    indices = {}
    fib = [1,1]; MOD = int(stdin.readline())
    counter = 2;
    while True:
        result = (fib[-1] + fib[-2]) % MOD
        fib.append(result)
        if result in indices:
            counter = indices[result]
            break
        indices[result] = counter
        counter += 1
    stdout.write(f"{counter}\n")
