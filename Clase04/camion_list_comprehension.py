from pprint import pprint
import csv

f = open('../Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)
select = ['nombre', 'cajones', 'precio']
indices = [headers.index(ncolumna) for ncolumna in select]
camion = [{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]
pprint(camion)

