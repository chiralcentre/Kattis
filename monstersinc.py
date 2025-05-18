from sys import stdin,stdout

# code runs in O(N + max(N,Q)) time
N = int(stdin.readline())
monsters = [tuple(map(int,stdin.readline().split())) for _ in range(N)]
Q = int(stdin.readline())
curr_index,curr_strength = 0,int(stdin.readline())
prev = curr_strength
while curr_index < N and curr_strength >= monsters[curr_index][0]:
    curr_strength += monsters[curr_index][1]
    curr_index += 1
stdout.write(f"{curr_index}\n")
for i in range(Q - 1):
    x = int(stdin.readline())
    curr_strength += x - prev
    while curr_index < N and curr_strength >= monsters[curr_index][0]:
        curr_strength += monsters[curr_index][1]
        curr_index += 1
    prev = x
    stdout.write(f"{curr_index}\n")
