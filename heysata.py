from sys import stdin

n = int(stdin.readline())
k = stdin.readline().strip()
s = stdin.readline().strip()
print("Unnar fann hana!") if k in s else print("Unnar fann hana ekki!")