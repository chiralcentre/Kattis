from sys import stdin,stdout

N = int(stdin.readline())
prefix_count = {}
for i in range(N):
    phone_num = stdin.readline().strip()
    for j in range(1,len(phone_num) + 1):
        prefix = phone_num[:j]
        prefix_count[prefix] = prefix_count.get(prefix,0) + 1
for _ in range(int(stdin.readline())):
    query = stdin.readline().strip()
    stdout.write(f"{prefix_count.get(query,0)}\n")
