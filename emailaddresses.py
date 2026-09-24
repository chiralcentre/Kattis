def solve(email):
    at_indices = []
    for i in range(len(email)):
        if email[i] == "@":
            at_indices.append(i)
    # first error
    if not at_indices:
        return "@ symbol is missing."
    # second error
    if len(at_indices) > 1:
        idx = at_indices[1]
        second_line = " " * idx + "^--there is an extra @ symbol here."
        return email + "\n" + second_line
    # invariant: there is only 1 @ symbol now
    at_idx = at_indices[0]
    # third error
    if at_idx == 0:
        return "There is nothing before the @ symbol."
    # fourth error
    if at_idx == len(email) - 1:
        return email + "\n" + " " * len(email) + "^--there is nothing after the @ symbol."
    # fifth error
    if email[0] == ".":
        return "Email address starts with a dot."
    # sixth error
    if email[at_idx - 1] == ".":
        return email + "\n" + " " * (at_idx - 1) + "^--there is an extra dot here."
    # seventh error
    for i in range(1,len(email)):
        if email[i] == email[i - 1] and email[i] == ".":
            return email + "\n" + " " * (i - 1) + "^--there are consecutive dots here."
    # last error
    found = False
    for i in range(at_idx + 1,len(email)):
        if email[i] == ".":
            found = True
            break
    if not found:
        return "Top-level-domain is missing."
    return "All good."
print(solve(input().strip()))
