import csv

with open('u_mesh.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

sorted_rows = sorted(rows, key=lambda x: (float(x[0]), float(x[1]))) # Sort by first column, then second column

with open('initial_mesh.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(sorted_rows)