def solve(n):
    mapping = {1: "single", 2: "double", 3: "triple"}
    result = []
    for i in range(1,21):
        for j in range(1,21):
            for k in range(1,21):
                for a in range(4):
                    for b in range(4):
                        for c in range(4):
                            if a*i + b*j + c*k == n:
                                if a > 0:
                                    result.append(f"{mapping[a]} {i}")
                                if b > 0:
                                    result.append(f"{mapping[b]} {j}")
                                if c > 0:
                                    result.append(f"{mapping[c]} {k}")
                                return '\n'.join(score for score in result) 
    return "impossible"

n = int(input())
print(solve(n))

            
