import pandas as pd
import csv
# read the csv file
df = pd.read_csv('initial_grid.csv')
print("DuplicateGrid")

# drop the duplicate entries
df = df.drop_duplicates()

# save the file with the same order
df.to_csv('u_grid.csv', index=False)



filename = 'u_grid.csv'

# read the file into a list of rows
with open(filename, 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# write the remaining rows back to the file, excluding the first row
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows[1:])

