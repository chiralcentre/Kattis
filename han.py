from sys import stdin,stdout

#every query is answered in constant time, total O(Q) time complexity
curr,prev,d,counter = 0,0,1,[0 for i in range(26)]
for _ in range(int(stdin.readline())):
    query = stdin.readline().split()
    n = int(query[1])
    diff = n - prev
    if diff >= 26:
        for i in range(26):
            counter[i] += diff // 26
        diff %= 26
    for i in range(diff):
        counter[curr] += 1
        curr = (curr + d) % 26
    prev = n
    if query[0] == "UPIT":
        stdout.write(f"{counter[ord(query[2]) - 97]}\n")
    else:
        d *= -1
        curr = (curr + d * 2) % 26
        
