from sys import stdin,stdout

N = int(stdin.readline())
# strains A,B,C are denoted by 1,2,3 respectively
vaccinated,control = {1:0,2:0,3:0},{1:0,2:0,3:0}
vaccinated_total,control_total = 0,0

for _ in range(N):
    participant = stdin.readline().strip()
    if participant[0] == 'Y': #vaccinated
        vaccinated_total += 1
        for i in range(1,4):
            if participant[i] == 'Y':
                vaccinated[i] += 1
    else: #control
        control_total += 1
        for i in range(1,4):
            if participant[i] == 'Y':
                control[i] += 1

for virus in range(1,4):
    vaccine_infections,control_infections = vaccinated[virus]/vaccinated_total,control[virus]/control_total
    stdout.write('Not Effective\n') if vaccine_infections >= control_infections else stdout.write(f'{((control_infections-vaccine_infections)/control_infections)*100}\n')
