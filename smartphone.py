from sys import stdin,stdout

def longest_common_prefix(w1,w2):
    for i in range(min(len(w1),len(w2))):
        if w1[i] != w2[i]:
            return i
    return i + 1

for _ in range(int(stdin.readline())):
    w1,w2,w3,w4,w5 = [stdin.readline().strip() for _ in range(5)]
    #find number of moves required using first suggestion
    m1 = len(w3) + len(w1) - 2 * longest_common_prefix(w1,w3) + 1
    #find number of moves required using second suggestion
    m2 = len(w4) + len(w1) - 2 * longest_common_prefix(w1,w4) + 1
    #find number of moves required using third suggestion
    m3 = len(w5) + len(w1) - 2 * longest_common_prefix(w1,w5) + 1
    #find number of moves required without using suggestion
    m4 = len(w2) + len(w1) - 2 * longest_common_prefix(w1,w2)
    stdout.write(f"{min(m1,m2,m3,m4)}\n")
