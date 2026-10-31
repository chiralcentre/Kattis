from sys import stdin

def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]

def run(): 
    n = int(stdin.readline())
    perm = [str(i + 1) for i in range(n)]
    def ask():
        print(" ".join(perm), flush=True)
        k = int(stdin.readline())
        if k == n:
            raise SystemExit
        return k
    p = ask()
    # try every pair in sequence
    # when swapping two numbers, there are 9 cases
    # let f{i) = index of i in correct permutation
    # let c = number of correct bottles for current permutation, and p = number of correct bottles for last permutation
    # case 1: f(perm[i]) not in {i,j}, f(perm[j]) not in {i,j}, c = p
    # case 2: f(perm[i]) = i, f(perm[j]) not in {i,j}, c = p - 1
    # case 3: f(perm[i]) = j, f(perm[j]) not in {i,j}, c = p + 1
    # case 4: f(perm[i]) not in {i,j}, f(perm[j]) = i, c = p + 1
    # case 5: f(perm[i]) = i, f(perm[j]) = i (invalid case)
    # case 6: f(perm[i]) = j, f(perm[j]) = i, c = p + 2
    # case 7: f(perm[i]) not in {i,j}, f(perm[j]) = j, c = p - 1
    # case 8: f(perm[i]) = i, f(perm[j]) = j, c = p - 2
    # case 9: f(perm[i]) = j, f(perm[j]) = j (invalid case)
    for i in range(n - 1):
        one_deltas,two_deltas = [],[]
        for j in range(i + 1,n):
            swap(perm,i,j)
            d = ask() - p
            # case 3 and 4
            if d == 1:
                one_deltas.append(j)
            # case 6
            elif d == 2:
                two_deltas.append(j)
            swap(perm,i,j)
        if not one_deltas and not two_deltas: # perm[i] is in the correct place
            continue
        star,d = None,0
        # there is always only 1 +2 delta or 2 +1 deltas
        if len(two_deltas) == 1:
            star = two_deltas[0]
            d = 2
        else:
            # either f(perm[i]) = c1 or f(perm[c1]) = i
            # either f(perm[i]) = c2 or f(perm[c2]) = i
            # do the swap (perm[i],perm[c1],perm[c2]) -> (perm[c1],perm[c2],perm[i])
            # 1. f(perm[i]) = c1, f(perm[i]) = c2 (not possible)
            # 2. f(perm[i]) = c1, f(perm[c2]) = i (0)
            # 3. f(perm[c1]) = i, f(perm[i]) = c2 (+3, +2)
            # 4. f(perm[c1]) = i, f(perm[c2]) = i (not possible)
            c1,c2 = one_deltas
            a,b,c = perm[i],perm[c1],perm[c2]
            perm[i],perm[c1],perm[c2] = b,c,a
            s = ask()
            perm[i],perm[c1],perm[c2] = a,b,c
            star = c1 if s - p >= 2 else c2
            d = 1
        swap(perm,i,star)
        p += d
    curr = ask()

if __name__ == "__main__":
    run()
