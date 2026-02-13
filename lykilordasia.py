words = input().split()
output = []
for w in words:
    has_numeric,has_letter = False,False
    for char in w:
        if char.isnumeric():
            has_numeric = True
        elif char.isalpha():
            has_letter = True
    if has_numeric and has_letter:
        output.append("*" * len(w))
    else:
        output.append(w)
print(" ".join(output))
            
