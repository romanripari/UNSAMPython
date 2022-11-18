# %%
def fibonacci(n):
    """
    Toma un entero positivo n y
    devuelve el n-ésimo número de Fibonacci
    donde F(0) = 0 y F(1) = 1.
    """
    def fibonacci_aux(n, dict_fibo):
        """
        Calcula el n-ésimo número de Fibonacci de forma recursiva
        utilizando un diccionario para almacenar los valores ya computados.
        dict_fibo es un diccionario que guarda en la clave 'k' el valor de F(k)
        """
        if n in dict_fibo.keys():
            F = dict_fibo[n]
        else:
            # Le doy a F el valor de la suma de los dos fib anteriores
            F = fibonacci_aux(n-1, dict_fibo)[0] + fibonacci_aux(n-2, dict_fibo)[0]
            # Guardo en el diccionario n el valor F para no calcular luego.
            dict_fibo[n] = F
        #Retorno el valor de F y el diccionario
        return  F, dict_fibo 

    dict_fibo = {0:0, 1:1} 
    F, dict_fibo = fibonacci_aux(n, dict_fibo)
    return F 

for fib in range(10):
    print(fibonacci(fib))