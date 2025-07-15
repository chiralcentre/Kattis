from sys import stdin,stdout

def add_to_digits(num, digits):
    while num > 0:
        r = num % 10
        digits[r] += 1
        num //= 10
    return digits

for _ in range(int(stdin.readline())):
    first_line = stdin.readline().strip()
    second_line = stdin.readline().strip()
    n = int(second_line.split()[0])
    digits = [0 for i in range(10)]
    seen = 0
    while seen < n:
        line = stdin.readline().strip()
        if line[0] == "+":
            op,s,e,j = line.split()
            s,e,j = int(s),int(e),int(j)
            for k in range(s,e + j,j):
                digits = add_to_digits(k,digits)
            seen += (e - s) // j + 1
        else:
            digits = add_to_digits(int(line),digits)
            seen += 1
    stdout.write(f"{first_line}\n")
    stdout.write(f"{second_line}\n")
    total = 0
    for i in range(10):
        total += digits[i]
        stdout.write(f"Make {digits[i]} digit {i}\n")
    stdout.write(f"In total {total} digit")
    stdout.write("s\n") if total > 1 else stdout.write("\n")
    

