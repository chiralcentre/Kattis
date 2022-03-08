from sys import stdin,stdout

for line in stdin:
    record = line.split()
    values,total,strings = 0,0,[]
    for item in record:
        try:
            total += float(item)
            values += 1
        except ValueError:
            strings.append(item)
    name = ' '.join(strings)
    stdout.write(f'{total/values} {name}\n')
