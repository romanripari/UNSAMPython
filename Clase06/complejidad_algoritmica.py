
# def algo(lista, m):
#     for p in lista:
#         for q in lista:
#             if m == p * q :
#                 print ( " %d= %d* %d " %(m, p , q ) )

# algo(range(1000000), 120000)

def incrementar(s):
    veces = 0
    carry = 1
    l = len(s)

    for i in range(l-1,-1,-1):
        veces +=1
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s
    
def listar_secuencias(n):
    lista = [0]*n
    veces = 0
    while 0 in lista:
        veces += 1
        incrementar(lista)
    print(lista)
    print(veces)

def run():
    # incrementar(list(range(1000)))
    listar_secuencias(15)
if __name__ == "__main__":
    run()