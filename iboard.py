from sys import stdin,stdout

for line in stdin:
    line = line.strip("\n")
    is_left_pressed,is_right_pressed = False,False
    for char in line:
        code = bin(ord(char))[2:] # remove 0b prefix
        if len(code) < 7:
            code += "0" * (7 - len(code)) # fill up to 7 bits
        rev_code = code[::-1]
        for bit in rev_code:
            if bit == "0":
                is_left_pressed = not is_left_pressed
            else:
                is_right_pressed = not is_right_pressed
    stdout.write("trapped\n") if is_left_pressed or is_right_pressed else stdout.write("free\n")
        
    
