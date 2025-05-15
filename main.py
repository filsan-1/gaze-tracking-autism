import csv
import os

FILE = "gaze_fixations.csv"

if not os.path.exists(FILE):
    with open(FILE, 'w', newline='') as f:
        csv.writer(f).writerow(['timestamp', 'target', 'x', 'y'])

def log_fixation_data(ts, target, pt):
    with open(FILE, 'a', newline='') as f:
        csv.writer(f).writerow([ts, target, int(pt[0]), int(pt[1])])

