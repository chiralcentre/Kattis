from sys import stdin,stdout

n = int(stdin.readline())
lectures,coffee,awake = stdin.readline().strip(),0,0
for i in range(n):
    if lectures[i] == "0":
        if coffee > 0:
            awake += 1
        coffee -= 1
    else:
        awake += 1
        coffee = 2
stdout.write(f"{awake}")
