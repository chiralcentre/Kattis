from sys import stdin,stdout

win = {"R": "S", "P": "R", "S": "P"}
while True:
    first,second = stdin.readline().strip(),stdin.readline().strip()
    if first == "E" and second == "E":
        break
    p1,p2 = 0,0
    for i in range(len(first)):
        if win[first[i]] == second[i]:
            p1 += 1
        elif win[second[i]] == first[i]:
            p2 += 1
    stdout.write(f"P1: {p1}\n")
    stdout.write(f"P2: {p2}\n")
