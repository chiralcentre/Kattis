base = {"0": 0,"1": 1,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,
        "A": 10,"C": 11,"D": 12,"E": 13,"F": 14,"H": 15,"J": 16,"K": 17,"L": 18,"M":19,
        "N": 20,"P": 21,"R": 22,"T": 23,"V": 24,"W": 25,"X": 26}
confusing_digits = {'B':'8',
                    'G':'C',
                    'I':'1',
                    'O':'0',
                    'Q':'0',
                    'S':'5',
                    'U':'V',
                    'Y':'V',
                    'Z':'2'}

for _ in range(int(input())):
    K,data = input().split()
    UCN,entered_check_digit = list(data[:8]),data[8]
    for char in UCN:
        if char in confusing_digits:
            char = confusing_digits[char]
    computed_check_digit = list(base.keys())[(2*base[UCN[0]] + 4*base[UCN[1]] + 5*base[UCN[2]] + 7*base[UCN[3]] + 8*base[UCN[4]] + 10*base[UCN[5]] + 11*base[UCN[6]] + 13*base[UCN[7]])%27]
    decimal_representation = base[UCN[0]]*27**7 + base[UCN[1]]*27**6 + base[UCN[2]]*27**5 + base[UCN[3]]*27**4 + base[UCN[4]]*27**3 + base[UCN[5]]*27**2 + base[UCN[6]]*27**1 + base[UCN[7]]
    print(f'{K} {decimal_representation}') if computed_check_digit == entered_check_digit else print(f'{K} Invalid')
        
