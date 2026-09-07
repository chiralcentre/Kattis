from math import log

def format_n(d):
    #check if power is integer or decimal
    if abs(int(d) - d) <= EPSILON: 
        if d == 0:
            return ""
        elif d == 1:
            return "n"
        else:
            return f"n^{int(d)}"
    else: #power is decimal, round to 1 d.p.
        return f"n^{d:.1f}"
    
def format_log_n(k):
    if k == -1:
        return "log log n"
    elif k == 1:
        return "log n"
    elif k <= 0:
        return ""
    else:
        return f"log^{k} n"

def format_log_n_literal(k):
    if k == 0:
        return ""
    elif k == 1:
        return "log n"
    else:
        return f"log^{k} n"
    
EPSILON = 10**(-10)
a,b,c,d,k = input().split()
a,k = int(a),int(k)
b,c,d = float(b),float(c),float(d)
#change of base formula to calculate exponent
exponent = log(a)/log(b)
diff = d - exponent
#Case 1 of Master Theorem, log_{b}(a) > d
#value of k does not matter since polynomials grow faster than logarithms
if diff < 0:
    print(f"{format_n(exponent)}")
#Case 2 of Master Theorem
elif abs(diff) <= EPSILON:
    first = format_n(d)
    if k >= 0:
        k += 1
    second = format_log_n(k)
    if first == "":
        print(f"{second}")
    else:
        print(f"{first} {second}")
#Case 3 of Master Theorem, log_{b}(a) < d
#for regularity condition to be satisfied, a/(b^d) < 1, which is already fulfilled since log_{b}(a) < d
else:
    first = format_n(d)
    second = format_log_n_literal(k)
    if second == "":
        print(f"{first}")
    else:
        print(f"{first} {second}")
