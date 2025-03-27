from sys import stdin,stdout

def solve(marks):
    diffs = set()
    for i in range(len(marks)):
        for j in range(i + 1, len(marks)):
            d = marks[j] - marks[i]
            if d not in diffs:
                diffs.add(d)
            else:
                return "not a ruler"
    H = max(marks)
    missing = [i for i in range(1, H + 1) if i not in diffs]
    if missing:
        return f"missing {' '.join(str(num) for num in missing)}"
    else:
        return "perfect"
    
for line in stdin:
    marks = sorted(map(int,line.split()))
    stdout.write(f"{solve(marks)}\n")
