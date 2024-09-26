from sys import stdin,stdout

def freq_counter(num):
    counter = {}
    for char in str(num):
        counter[char] = counter.get(char,0) + 1
    return counter

def merge_counters(c1,c2):
    res = {}
    for key, value in c1.items():
        res[key] = value
    for key, value in c2.items():
        res[key] = res.get(key,0) + value
    return res

A,B = map(int,stdin.readline().split())
output = []
for i in range(A,B + 1):
    for j in range(i + 1,B + 1):
        prod = i * j
        c1,c2,c3 = freq_counter(i),freq_counter(j),freq_counter(prod)
        if c3 == merge_counters(c1,c2):
            output.append(f"x = {i}, y = {j}, xy = {prod}\n")
stdout.write(f"{len(output)} digit-preserving pair(s)\n")
stdout.write("".join(output))
