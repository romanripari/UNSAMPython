with open('./Data/camion.csv', 'rt') as f:
    data = f.read()

print(data)

f = open('./Data/camion.csv', 'rt')
headers = next(f)
headers
for line in f:
    row = line.split(',')
    print(row)
f.close()

import gzip
with gzip.open('./Data/camion.csv.gz', 'rt') as f:
        for line in f:
            print(line, end = '')

