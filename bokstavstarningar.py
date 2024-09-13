from sys import stdin

# use minimum remaining values heuristic
def select_unassigned_variable(domains,word,assignment):
    best,chosen = pow(10,9), None
    for i in range(len(word)):
        if i not in assignment:
            L = len(domains[word[i]])
            if L < best:
                best,chosen = L,i
    return chosen

def remove_inconsistent_values(domains,word,latest_assignment,assignment):
    removed = {}
    for key in domains:
        if latest_assignment in domains[key]:
            if key in removed:
                removed[key].append(latest_assignment)
            else:
                removed[key] = [latest_assignment]
            domains[key].remove(latest_assignment)
    for i in range(len(word)):
        if i not in assignment and len(domains[word[i]]) == 0:
            return removed,False
    return removed,True

def backtrack(domains,word,assignment):
    # check if assignment is complete
    if len(assignment) == len(word):
        return assignment
    var = select_unassigned_variable(domains,word,assignment)
    values = [v for v in domains[word[var]]]
    for v in values:
        assignment[var] = v
        # remove inconsistent values in domains,forward checking
        removed,possible = remove_inconsistent_values(domains,word,v,assignment)
        result = None
        if possible:
            result = backtrack(domains,word,assignment)
        # add back values removed from domain
        for key,lst in removed.items():
            for v in lst:
                domains[key].add(v)
        if result != None:
            return result
        assignment.pop(var)
    return None

def solve_CSP(word, domains):
    return backtrack(domains, word, {})
    
N,K,M = map(int,stdin.readline().split())
letters = {}
for i in range(N):
    faces = stdin.readline().strip()
    for f in faces:
        if f in letters:
            letters[f].add(i)
        else:
            letters[f] = {i}
valid_words = 0
for i in range(M):
    w = stdin.readline().strip()
    res = solve_CSP(w, letters)
    if res:
        valid_words += 1
print(valid_words)
