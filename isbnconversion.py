from sys import stdin,stdout

def convert_int(char):
    return int(char) if char != "X" else 10

def verify(parts,original):
    # check if there is up to 3 hyphens
    # check if it begins or ends with a hyphen or contains consecutive hyphens 
    if len(parts) > 4 or "" in parts:
        return False
    # if there are 3 hyphens, check that the checksum digit is separated from preceding digit
    if len(parts) == 4 and len(parts[-1]) != 1:
        return False
    # check if there are 10 digits left after parsing
    if len(original) != 10:
        return False
    # check only the last digit is X
    occur = original.count("X")
    if occur > 1 or (occur == 1 and original[-1] != "X"):
        return False
    checksum = sum(convert_int(original[i]) * (10 - i) for i in range(len(original)))
    return not checksum % 11

for _ in range(int(stdin.readline())):
    code = stdin.readline().strip()
    parts = code.split("-")
    original = "".join(p for p in parts)
    if verify(parts,original):
        new  = "978" + original[:-1]
        checksum = sum(convert_int(new[i]) * (1 + (i % 2) * 2) for i in range(len(new)))
        cs_digit = 10 - (checksum % 10)
        # cannot end with a 10 in ISBN-13
        if cs_digit == 10:
            cs_digit = 0
        code = "978-" + code[:-1] + str(cs_digit)
        stdout.write(f"{code}\n")
    else:
        stdout.write("invalid\n")
