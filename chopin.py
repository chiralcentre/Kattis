from sys import stdin,stdout

alt = {"A#": "Bb", "Bb": "A#", "C#": "Db", "Db": "C#",
             "D#": "Eb", "Eb": "D#", "F#": "Gb", "Gb": "F#",
             "G#": "Ab", "Ab": "G#"}

counter = 0
for line in stdin:
    counter += 1
    note,tone = line.strip().split()
    if note in alt:
        stdout.write(f"Case {counter}: {alt[note]} {tone}\n")
    else:
        stdout.write(f"Case {counter}: UNIQUE\n")
    
