from sys import stdin,stdout

population,species = 0,{}
for line in stdin:
    line = line.strip()
    population += 1
    species[line] = 1 if line not in species else species[line] + 1
stdout.write('\n'.join(f'{s} {str(100*species[s]/population)}' for s in sorted(species)))
