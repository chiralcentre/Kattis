from sys import stdin,stdout

# every person faces either left (<) or right (>)
# represent this with an array A: A[i] = 1 if person i faces right, else 0
# values[i] = |{j < i: A[j] = 1}| + |{j > i: A[j] = 0}|
# goal: recover some valid A matching all given values[i], or prove none exists
# values[i + 1] - values[i] = |{j < i + 1: A[j] = 1}| + |{j > i + 1: A[j] = 0}| - |{j < i: A[j] = 1}| - |{j > i: A[j] = 0}|
# |{j < i + 1: A[j] = 1}| - |{j < i: A[j] = 1}| = A[i]
# |{j > i + 1: A[j] = 0}| - |{j > i: A[j] = 0}| = -1 if A[i + 1] = 0, else 0 = A[i + 1] - 1
# values[i + 1] - values[i] = A[i] + A[i + 1] - 1
# since A[i],A[i + 1] is either 0 or 1, -1 <= values[i + 1] - values[i] <= 1
# if any consecutive difference is outside the range -1 to 1, it is immediately impossible'
# values[i + 1] - values[i] = 1 -> A[i] + A[i + 1] = 2 -> A[i] = 1, A[i + 1] = 1
# values[i + 1] - values[i] = 0 -> A[i] + A[i + 1] = 1 -> A[i] = 0, A[i + 1] = 1 or A[i] = 1, A[i + 1] = 0
# values[i + 1] - values[i] = -1 -> A[i] + A[i + 1] = 0 -> A[i] = 0, A[i + 1] = 0
# approach: fix A[0] as either 0 or 1, and propagate accordingly based on differences
# time complexity: O(n)
def solve(n,values):
    diffs = []
    for i in range(n - 1):
        d = values[i + 1] - values[i]
        if not -1 <= d <= 1:
            return False,None
        diffs.append(d)
    for start in (0,1):
        A = [start]
        ok = True
        for d in diffs:
            if d == -1:
                if A[-1] != 0:
                    ok = False
                    break
                A.append(0)
            elif d == 1:
                if A[-1] != 1:
                    ok = False
                    break
                A.append(1)
            else: # flip
                A.append(1 - A[-1])
        if not ok:
            continue
        # perform verification
        # propagation only ensures the differences are satisfied
        # absolute nervousness values for A may differ from original array
        L = [0 for _ in range(n)] # L[i] = number of people looking left towards person i
        R = [0 for _ in range(n)] # R[i] = number of people looking right towards person i
        for i in range(1,n):
            if A[i - 1] == 1:
                R[i] = R[i - 1] + 1
            else:
                R[i] = R[i - 1]
        for i in range(n - 2,-1,-1):
            if A[i + 1] == 0:
                L[i] = L[i + 1] + 1
            else:
                L[i] = L[i + 1]
        for i in range(n):
            if L[i] + R[i] != values[i]:
                ok = False
                break
        if not ok:
            continue
        return True,"".join(">" if a == 1 else "<" for a in A)
    return False,None

n = int(stdin.readline())
values = list(map(int,stdin.readline().split()))
is_possible,output = solve(n,values)
if is_possible:
    stdout.write("possible\n")
    stdout.write("".join(output))
else:
    stdout.write("impossible\n")
