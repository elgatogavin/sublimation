import csv
import csv
import numpy as np
import cv2
from PIL import Image


def remap(val, old_min, old_max, new_min, new_max):
    # Convert val from the old range to the range [0, 1]
    val_norm = (val - old_min) / (old_max - old_min)

    # Convert val from the range [0, 1] to the new range
    val_new = val_norm * (new_max - new_min) + new_min

    return val_new

with open('mesh.csv') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    src_points = np.float32([[float(row[0]), float(row[1])] for row in rows])

print("ScaleMesh")
# Transform the old points to the new origin
new_points = []
for point in src_points:
    new_x = remap(point[0], 0,110, 0, 5197)
    new_y = remap(point[1],0,125,0, 5906)
    new_points.append([new_x, new_y])

with open('mesh_final.csv', 'w', newline='') as f:
    # Write the new points to the CSV file
    writer = csv.writer(f)
    for point in new_points:
        writer.writerow(point)