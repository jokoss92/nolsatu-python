import csv

siswa = [
    ('arslan', 'A', 90),
    ('bayu', 'B', 85),
    ('niko', 'A', 80),
    ('abdul', 'B', 90),
    ('dahlan', 'C', 70)
]

f = open('siswa.csv', 'w')

w = csv.writer(f)

w.writerow(('Nama', 'Kelas', 'Nilai'))

for s in siswa:
    w.writerow(s)

f.close()