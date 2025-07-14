from sys import stdin,stdout

note_fingers = {
    "c":  [1, 2, 3, 6, 7, 8, 9],       
    "d":  [1, 2, 3, 6, 7, 8],      
    "e":  [1, 2, 3, 6, 7],       
    "f":  [1, 2, 3, 6],         
    "g":  [1, 2, 3],            
    "a":  [1, 2],
    "b":  [1],               
    "C":  [2],                
    "D":  [0, 1, 2, 3, 6, 7, 8],    
    "E":  [0, 1, 2, 3, 6, 7],    
    "F":  [0, 1, 2, 3, 6],       
    "G":  [0, 1, 2, 3],       
    "A":  [0, 1, 2],          
    "B":  [0, 1],
}

for _ in range(int(stdin.readline())):
    presses = [0 for i in range(10)]
    song = stdin.readline().strip()
    if song:
        fingers = set()
        for finger in note_fingers[song[0]]:
            fingers.add(finger)
            presses[finger] += 1
        for i in range(1,len(song)):
            new_fingers = set()
            for finger in note_fingers[song[i]]:
                if finger not in fingers:
                    presses[finger] += 1
                new_fingers.add(finger)
            fingers = new_fingers
    stdout.write(" ".join(str(num) for num in presses))
    stdout.write("\n")
