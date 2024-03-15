from sys import stdin,stdout

def solve():
    N = int(stdin.readline())
    low,high = 1,N
    for i in range(16):
        if high - low >= 4:
            step = (high - low + 1) >> 2
            rem = (high - low + 1) % 4
            q1 = low + step + (rem == 3)
            q2 = q1 + step - 1 + (rem >= 2)
            q3 = q2 + step
            print(f"Q {low} {q2} {q1} {q3}",flush = True)
            w1,w2 = map(int,stdin.readline().split())
            if w1 == 1 and w2 == 1:
                if q1 == q2:
                    return f"A {q2}"
                low = q1 - 1
                high = q2 + 1
            elif w1 == 1 and w2 == 0:
                if q1 - low <= 1:
                    return f"A {low}"
                low = max(1,low - 1)
                high = q1
            elif w1 == 0 and w2 == 1:
                if q3 - q2 <= 1:
                    return f"A {q3}"
                low = q2
                high = q3 + 1
            else:
                if high - q3 == 1:
                    return f"A {high}"
                low = q3
                high = min(high + 1,N)
        else:
            print(f"Q {low} {low + 1} {low + 1} {min(low + 2,high)}",flush = True)
            w1,w2 = map(int,stdin.readline().split())
            if w1 == 1 and w2 == 1:
                return f"A {low + 1}"
            elif w1 == 1 and w2 == 0:
                return f"A {low}"
            elif w1 == 0 and w2 == 1:
                return f"A {low + 2}"
            else:
                return f"A {low + 3}"
print(solve())
