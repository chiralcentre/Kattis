from sys import stdin,stdout

numbers = [int(stdin.readline()) for _ in range(9)]
for a in range(9):
    for b in range(a+1,9):
        for c in range(b+1,9):
            for d in range(c+1,9):
                for e in range(d+1,9):
                    for f in range(e+1,9):
                        for g in range(f+1,9):
                            lst = [a,b,c,d,e,f,g]
                            if sum(numbers[i] for i in lst) == 100:
                                for i in lst:
                                    stdout.write(f"{numbers[i]}\n")
    
