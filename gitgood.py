from sys import stdin,stdout

path,path_name,output = [],"",set()
for _ in range(int(stdin.readline())):
    cmd, arg = stdin.readline().split()
    if cmd == "cd":
        if arg == "..":
            path.pop()
        else:
            path.append(arg)
        path_name = '/'.join(path)
    else:
        file = f"{path_name}/{arg}" if path_name != "" else arg
        output.add(file)
for file in sorted(output):
    stdout.write(f"git add {file}\n")
stdout.write("git commit\ngit push\n")
        
