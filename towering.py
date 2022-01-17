# O(n^3) is ok for small input
def find_towers(boxes,h1,h2):
    for i in range(5):
        for j in range(i+1,6):
            for k in range(j+1,6):
                if boxes[i] + boxes[j] + boxes[k] == h1:
                    a,b,c = boxes[i],boxes[j],boxes[k]
                    combinations = [a,b,c]
                    boxes.remove(a); boxes.remove(b); boxes.remove(c);
                    combinations += boxes # no need to sort remaining numebrs as they are already in reverse order
                    return combinations

line = list(map(int,input().split()))
boxes,h1,h2 = sorted(line[:6],reverse = True),line[6],line[7]
                
print(' '.join(list(map(str,find_towers(boxes,h1,h2)))))
            
                
