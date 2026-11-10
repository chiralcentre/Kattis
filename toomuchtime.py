from sys import stdin,stdout
from math import ceil

ds,dataset_size,dataset_window,dataset_curr = 0,0,0,0
start,total_secs,sec_curr = True,0,0
while True:
    num = int(stdin.readline())
    if start and num == 0:
        break
    if start:
        ds += 1
        start,dataset_window,dataset_curr = False,0,0
        total_secs,sec_curr = 0,0
        dataset_size = num
        stdout.write(f"Output for data set {ds}, {dataset_size} bytes:\n")
    else:
        sec_curr += 1
        dataset_window += num
        if sec_curr % 5 == 0:
            total_secs += 5
            sec_curr = 0
            if dataset_window == 0:
                stdout.write("   Time remaining: stalled\n")
            else:
                avg_speed = dataset_window / 5
                dataset_curr += dataset_window
                dataset_window = 0
                r = dataset_size - dataset_curr
                stdout.write(f"   Time remaining: {ceil(r / avg_speed)} seconds\n")
        if dataset_curr + dataset_window == dataset_size:
            start = True
            stdout.write(f"Total time: {total_secs + sec_curr} seconds\n")
        
