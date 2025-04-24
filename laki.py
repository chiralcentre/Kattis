from math import gcd,sqrt

def mod(a, m):
    return ((a % m) + m) % m

def extended_gcd(a, b):
    x, y = 1, 0
    xx, yy = 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - q * xx
        y, yy = yy, y - q * yy
    return a, x, y

def mod_inverse(b, m):
    g, x, _ = extended_gcd(b, m)
    if g != 1:
        return -1
    return mod(x, m)

def mod_exp(x, y):
    ans = 1
    while y > 0:
        if y % 2 == 1:
            ans *= x
        y //= 2
        x *= x
    return ans

def prime_factor(n):
    factors = {}
    while n % 2 == 0:
        factors[2] = factors.get(2,0) + 1
        n //= 2
    for i in range(3, sqrt(n) + 1, 2):
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
    if n > 2:
        factors[n] = 1
    return factors

def crt(r, m):
    mt = 1
    for mi in m:
        mt *= mi
    x = 0
    for ri, mi in zip(r, m):
        Mi = mt // mi
        inv = mod_inverse(Mi, mi)
        a = mod(ri * inv, mi)
        x = mod(x + a * Mi, mt)
    return x

periodic_table = {
    "H": 1, "He": 2,
    "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10,
    "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17, "Ar": 18,
    "K": 19, "Ca": 20, "Sc": 21, "Ti": 22, "V": 23, "Cr": 24, "Mn": 25, "Fe": 26, "Co": 27, "Ni": 28,
    "Cu": 29, "Zn": 30, "Ga": 31, "Ge": 32, "As": 33, "Se": 34, "Br": 35, "Kr": 36,
    "Rb": 37, "Sr": 38, "Y": 39, "Zr": 40, "Nb": 41, "Mo": 42, "Tc": 43, "Ru": 44, "Rh": 45, "Pd": 46,
    "Ag": 47, "Cd": 48, "In": 49, "Sn": 50, "Sb": 51, "Te": 52, "I": 53, "Xe": 54,
    "Cs": 55, "Ba": 56, "La": 57, "Ce": 58, "Pr": 59, "Nd": 60, "Pm": 61, "Sm": 62, "Eu": 63, "Gd": 64,
    "Tb": 65, "Dy": 66, "Ho": 67, "Er": 68, "Tm": 69, "Yb": 70, "Lu": 71,
    "Hf": 72, "Ta": 73, "W": 74, "Re": 75, "Os": 76, "Ir": 77, "Pt": 78, "Au": 79, "Hg": 80,
    "Tl": 81, "Pb": 82, "Bi": 83, "Po": 84, "At": 85, "Rn": 86,
    "Fr": 87, "Ra": 88, "Ac": 89, "Th": 90, "Pa": 91, "U": 92, "Np": 93, "Pu": 94, "Am": 95, "Cm": 96,
    "Bk": 97, "Cf": 98, "Es": 99, "Fm": 100, "Md": 101, "No": 102, "Lr": 103,
    "Rf": 104, "Db": 105, "Sg": 106, "Bh": 107, "Hs": 108, "Mt": 109, "Ds": 110, "Rg": 111,
    "Cn": 112, "Nh": 113, "Fl": 114, "Mc": 115, "Lv": 116, "Ts": 117, "Og": 118
}

reverse_periodic_table = {value: key for key, value in periodic_table.items()}

int_to_mayan = {i: chr(0x1D2E0 + i) for i in range(20)}

mayan_to_int = {chr(0x1D2E0 + i): i for i in range(20)}

hardcoded = {"tragedy + time": "comedy", "repetition + repetition": "learning", "fire + water": "steam", "red + blue": "purple",
             "icelander + deadline": "procrastination", "throat + potato": "danish", "kattis + program": "verdict", "problem + solution": "AC",
             "contest + geometry": "WA", "nonsense + annoyance": "this problem", 
             }

line = input().strip()
split_line = line.split(" + ")
is_numeric = all(item.isnumeric() for item in split_line)
some_numeric = any(item.isnumeric() for item in split_line)
if is_numeric: # number addition
    # simple number addition
    try:
        print(eval(line))
    except: # Mayan number addition
        total = 0
        for item in split_line:
            value = sum(mayan_to_int[item[i]] * pow(20, len(item) - i - 1) for i in range(len(item)))
            total += value
        mayan_repr = []
        if total == 0:
            mayan_repr.append(int_to_mayan[0])
        else:
            while total:
                total,r = divmod(total,20)
                mayan_repr.append(int_to_mayan[r])
        print("".join(str(num) for num in reversed(mayan_repr)))
elif '0x' in line: # hexadecimal
    print(hex(eval(line)))
elif '"' in line: # string
    print(eval(line))
elif 'log' in line: # logarithm addition
    ans = 1
    for item in split_line:
        num = int(item[4:-1])
        ans *= num
    print(f"log({ans})")
elif 'i' in line and some_numeric: # imaginary number addition
    line = line.split(" + ")
    real_part,imaginary_part = 0,0
    for item in line:
        if "i" in item:
            imaginary_part += int(item[:-1])
        else:
            real_part += int(item)
    print(f"{real_part} + {imaginary_part}i")
elif "{" in line: # set addition
    line = line.split(" + ")
    ans = set()
    for i in range(len(line)):
        if len(line[i]) == 2: # empty set:
            item = set()
        else:
            item = eval(line[i])
        ans = ans.union(item)
    ans = sorted(ans)
    print("{",end = '')
    print(", ".join(str(num) for num in ans), end = "")
    print("}")
elif "mod" in line: # chinese remainder theorem
    r,m,LCM = [],[],1
    for item in split_line:
        a,b = map(int,item.split(" mod "))
        LCM = LCM * b // gcd(LCM,b)
        r.append(a)
        m.append(b)
    print(f"{crt(r,m)} mod {LCM}")
elif any(item in periodic_table for item in split_line): # periodic table addition
    num = sum(periodic_table[item] for item in split_line)
    print(reverse_periodic_table[num])
else:
    print(hardcoded[line])

