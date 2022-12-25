from sys import stdin,stdout

projects,signed,temp,p = {},set(),set(),""
multiple = set()
for line in stdin:
    line = line.strip()
    if line.isupper(): #title of project
        projects[line] = set()
        p = line
        for s in temp:
            signed.add(s)
        temp = set()
    elif line.islower(): #student
        if line not in signed:
            projects[p].add(line)
            temp.add(line)
        else:
            multiple.add(line)
    if line[0] == "1":
        output = list(projects.items())
        for i in range(len(output)):
            for student in multiple:
                if student in output[i][1]:
                    output[i][1].remove(student)
        output.sort(key = lambda x: (-len(x[1]),x[0]))
        for program,s in output:
            stdout.write(f"{program} {len(s)}\n")
        projects,signed,p = {},set(),""
        temp,multiple = set(),set()
    if line[0] == "0":
        break
