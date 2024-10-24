def solve(q1,q2,q3,q4,q5):
    a = q1
    b = q2
    c = q3
    # check if error lies in q1
    a = q4 - b - c
    if a + 2 * b + 3 * c == q5:
        return f"{a} {b} {c}"
    a = q1
    # check if error lies in q2
    b = q4 - a - c
    if a + 2 * b + 3 * c == q5:
        return f"{a} {b} {c}"
    b = q2
    # check if error lies in q3
    c = q4 - a - b
    if a + 2 * b + 3 * c == q5:
        return f"{a} {b} {c}"
    c = q3
    # check if error lies in q4
    if a + 2 * b + 3 * c == q5:
        return f"{a} {b} {c}"
    # check if error lies in q5
    if a + b + c == q4:
        return f"{a} {b} {c}"

# any three rows must be linearly independent
# this ensures if we remove the lie, we obtain a consistent overdetermined system of equations
q1,q2,q3,q4,q5 = 0,0,0,0,0
print("1 0 0")
q1 = int(input())
print("0 1 0")
q2 = int(input())
print("0 0 1")
q3  = int(input())
print("1 1 1")
q4 = int(input())
print("1 2 3")
q5 = int(input())
print(solve(q1,q2,q3,q4,q5))

    
