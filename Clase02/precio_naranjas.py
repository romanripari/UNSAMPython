with open('./Data/precios.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        if row[0] == "Naranja":
            print(f'El precio de la naranja es:  {row[1]}')

