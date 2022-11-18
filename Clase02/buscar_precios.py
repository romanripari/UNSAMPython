import sys

def buscar_precio(fruta: str) ->str:
    with open('../Data/precios.csv', 'rt') as f:
        for line in f:
            row = line.split(',')
            if row[0].lower() == fruta.lower():
                return f'El precio de la {fruta} es: {row[1]}'
        return f'{fruta} no figura en el listado de precios.'

# Si se ejecutar el archivo py con un argumento (fruta), entonces busca ese nombre.
# Si no, busca "Naranja"
if len(sys.argv) == 2:
    fruta = sys.argv[1]
else:
    fruta = "Naranja"

precio = buscar_precio(fruta)
print(precio)