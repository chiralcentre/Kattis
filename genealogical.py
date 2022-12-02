from sys import stdin,stdout

def write_ancestors(name,indent):
    if name in parent:
        for p in parent[name]:
            info = f"{p}\n"
            if p in birth:
                info = f"{p} {birth[p]} - {death[p]}\n" if p in death else f"{p} {birth[p]} -\n"
            stdout.write((indent + 2)* " " + info)
            write_ancestors(p,indent + 2)
        
            
def write_descendants(name,indent):
    if name in child:
        for c in sorted(child[name]):
            info = f"{c}\n"
            if c in birth:
                info = f"{c} {birth[c]} - {death[c]}\n" if c in death else f"{c} {birth[c]} -\n"
            stdout.write((indent + 2)* " " + info)
            write_descendants(c,indent + 2)   
        
birth,death = {},{}
parent,child = {},{}
first = True
for line in stdin:
    line = line.strip()
    if len(line) == 4: #QUIT command
        break
    if line[:5] == "BIRTH":
        line = line[6:].split(" : ")
        name,birthdate,mother,father = line[0],line[1],line[2],line[3]
        birth[name] = birthdate
        p = sorted([mother,father]) #sort parent names in alphabetical order
        parent[name] = p
        if mother not in child:
            child[mother] = [name]
        else:
            child[mother].append(name)
        if father not in child:
            child[father] = [name]
        else:
            child[father].append(name)
    elif line[:5] == "DEATH":
        line = line[6:].split(" : ")
        name,deathdate = line[0],line[1]
        death[name] = deathdate
    elif line[:9] == "ANCESTORS":
        if first: first = False
        else: stdout.write("\n")
        name = line[10:]
        stdout.write(f"ANCESTORS of {name}\n")
        write_ancestors(name,0)
    else: #DESCENDANTS command
        if first: first = False
        else: stdout.write("\n")
        name = line[12:]
        stdout.write(f"DESCENDANTS of {name}\n")
        write_descendants(name,0)
        
    
