from sys import stdin,stdout

def solve(n,elements):
    for i in range(1,n//2+1):
        solution_found = True
        for j in range(1,n//i):
            if elements[j*i-1] >= elements[(j+1)*i-1]:
                solution_found = False
                break
        if solution_found:
            return str(i)      
    return "ABORT!"

n = int(stdin.readline())
elements = list(map(int,stdin.readline().split()))
stdout.write(solve(n,elements))
    
