from sys import stdin,stdout

mappings = {"0": 0, "1": 1, "2": 2, "3": 3,
            "4": 4, "5": 5, "6": 6, "7": 7,
            "8": 8, "9": 9, "a": 10, "b": 11,
            "c": 12, "d": 13, "e": 14, "f": 15}

for line in stdin:
    i = 0
    while i < len(line):
        if i + 1 < len(line) and line[i:i+2].lower() == "0x":
            j = i + 2
            #maximum length of 8 means j - i <= 9
            while j < len(line) and j - i <= 9 and line[j].lower() in mappings:
                j += 1
            h = line[i + 2:j]
            d = sum(mappings[h[k].lower()] * pow(16,len(h) - k - 1) for k in range(len(h)))
            stdout.write(f"0x{h} {d}\n")
            i = j
        else:
            i += 1
