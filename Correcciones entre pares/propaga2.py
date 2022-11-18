def propagar(vector):
    
    propagado=vector
    l=len(vector)
    
    '''0 (nuevo), un 1 (encendido) o un -1 (carbonizado). El fuego se propaga inmediatamente 
    de un fósforo encendido a cualquier fósforo nuevo que 
    tenga a su lado. Los fósforos carbonizados no se encienden nuevamente.'''
    
    for i in range(0,l):
        if vector[i]==1:  # si el fosforo esta encendido
            j=i;k=i         # creo 2 subindices en la posicion de i
            while j<l-1:    #j asciende hasta l-1
                if propagado[j+1]==0: #solo si es nuevo
                    propagado[j+1]=1   # lo enciende
                    j=j+1           # continua ascendiendo en la propagacion
                else:      #hasta que k+1 != 0
                    break
            while k>=1:   #j desciende hasta 1
                if propagado[k-1]==0:   #solo si es nuevo
                    propagado[k-1]=1    # lo enciende
                    k=k-1      # continua descendiendo en la propagacion
                else:           #hasta que k-1 != 0
                    break    
        i+=1     #voy al siguiente fosforo
        
    return propagado

def run():
    print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))

# A este if entra si se ejecuta el archivo .py solo, pero NO si se importa como módulo.
if __name__ == "__main__":
    run()


#[ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
            
#z[1:]-z[:-1] #calcula todos los valores de z_{i+1}-z_{i}
#np.sum(z[1:]-z[:-1])
#∑𝑖=0𝑛(𝑧𝑖+1−𝑧𝑖)