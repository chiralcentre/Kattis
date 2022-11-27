from sys import stdin,stdout

while True:
    try:
        domain = stdin.readline().split()[1:]
        codomain = stdin.readline().split()[1:]
        n = int(stdin.readline())
        mappings,reverseMappings = set(),set()
        taken,values = set(),set()
        FUNCTION,surjective,injective = True,True,True
        for i in range(n):
            a,b = stdin.readline().split(" -> ")
            if a in mappings:
                FUNCTION = False
            if b in reverseMappings:
                injective = False
            mappings.add(a)
            reverseMappings.add(b)
        if not FUNCTION:
            stdout.write("not a function\n")
        else:
            if len(reverseMappings) != len(codomain):
                surjective = False
            if injective and surjective:
                stdout.write("bijective\n")
            elif injective and not surjective:
                stdout.write("injective\n")
            elif not injective and surjective:
                stdout.write("surjective\n")
            else:
                stdout.write("neither injective nor surjective\n")
    except:
        break
   
        
        
