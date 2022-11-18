from pprint import pprint


import csv
f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)


print(headers)
print(row)

def tupla(texto):
    # tupla con los valores en integer de todos los elementos de la lista generada por un .split()
    return tuple( [int(x) for x in texto.split("/")] )

types = [str, float, tupla, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))

pprint(record)
