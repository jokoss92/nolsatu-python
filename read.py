# import csv

# f = open('siswa.csv', 'r')

# reader = csv.reader(f)

# for row in reader:
#     print(row)

# f.close()

import csv

 

with open('siswa.csv', 'r') as f:

    reader = csv.reader(f)


for row in reader:

    print(row)