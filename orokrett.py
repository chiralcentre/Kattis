from sys import stdin

# NP complete problem to determines satisfiability of ANF expressions
# For ONF expressions, they are satisfiable so long as any clause does not contain a literal and its negation
def solve(line):
    clauses = line.split(" EDA ")
    for clause in clauses:
        P,N = set(),set()
        literals = clause[1:-1].split(" OG ")
        for L in literals:
            if L[0] == "!":
                N.add(L[1:])
            else:
                P.add(L)
        # satisfiable term found
        if not any(x in N for x in P):
            return "Jebb"
    return "Neibb"
    
print(solve(stdin.readline().strip()))

