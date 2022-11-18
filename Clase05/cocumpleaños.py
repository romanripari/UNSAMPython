
import random


def prob_cruzarse(N, Pers=30):
    algun_par = True
    personas = []
    for p in range(Pers):
        personas.append(random.randint( 1,365))
    if len(set(personas)) == Pers:
        algun_par = False
    return algun_par


def run():

    N = 10000
    # G = sum([prob_cruzarse(N) for i in range(N)])
    # prob = G/N
    # print(f'Podemos estimar la probabilidad de que en 30 personas haya dos que cunplan el mismo día es {prob:.6f}.')

    Pers = 0
    prob = 0.0
    while prob < 0.90:
        Pers +=1
        G = sum([prob_cruzarse(N, Pers) for i in range(N)])
        prob = G/N

    print(f'La mínima cantidad de personas necesarias para que haya 0.5 de probabilidad es: {Pers}.')

if __name__ == "__main__":
    run()
