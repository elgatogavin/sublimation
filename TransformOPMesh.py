import csv

# Define the old and new origins
old_origin = [0, 0]
new_origin = [55, -40.3]

# Open the CSV file containing the old points
with open('u_mesh.csv', 'r') as f:
    # Read the points from the CSV file
    reader = csv.reader(f)
    old_points = [list(map(float, row)) for row in reader]

print("transformMesh")
# Transform the old points to the new origin
new_points = []
for point in old_points:
    #print("point:", point)
    new_x = point[0] - old_origin[0] + new_origin[0]
    new_y = point[1] - old_origin[1] + new_origin[1]
    new_points.append([new_x, -1*new_y])

# Open a new CSV file to save the transformed points
with open('mesh.csv', 'w', newline='') as f:
    # Write the new points to the CSV file
    writer = csv.writer(f)
    for point in new_points:
        writer.writerow(point)