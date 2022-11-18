import csv
def parse_csv(nombre_archivo, select=None):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        # Lee los encabezados
        headers = next(rows)
        if select:
            indices = [headers.index(ncolumna) for ncolumna in select]
            select=headers
        else:
            indices=[]
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            if indices:
                # row= row[index] for ncolumna, index in zip(headers, indices)
                row= [row[index] for index in indices]
            registro= dict(zip(headers, row))
            registros.append(registro)
        return registros
