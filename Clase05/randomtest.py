import random
from pprint import pprint as pprint
# valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
# palos = ['oro', 'copa', 'espada', 'basto']
# naipes = [(valor,palo) for valor in valores for palo in palos]
# tres_cartas = random.sample(naipes,k=3)
# print(tres_cartas)

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]
random.shuffle(naipes)

n1 = naipes.pop()
n2 = naipes.pop()
n3 = naipes.pop()
print(f'Repartí el {n1[0]} de {n1[1]}, el {n2[0]} de {n2[1]} y el {n3[0]} de {n3[1]}. Quedan {len(naipes)} naipes en el mazo.')

for i in range(6):
    print(f'{random.normalvariate(0,1):.2f}', end=', ')
    
# random.seed()

# tirada=[]
# for i in range(5):
#     tirada.append(random.randint(1,6)) 

# print(tirada)

# caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
# print(random.choice(caras))
# print(random.choices(caras,k=5))
# # import random


# # def tirar():
# #     tirada=[]
# #     for i in range(5):
# #         tirada.append(random.randint(1,6))
# #     return tirada

# # def es_generala(tirada):
# #     generala = True
# #     numero = tirada[0]
# #     for t in tirada:
# #         if t != numero:
# #             generala = False
# #     return generala

# # def run():
# #     # tirada = tirar()
# #     # print (tirada)
# #     # print(es_generala(tirada))
# #     N = 10000000 
# #     G = sum([es_generala(tirar()) for i in range(N)])
# #     prob = G/N
# #     print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
# #     print(f'Podemos estimar la probabilidad de sacar generala servida en {prob*100:.6f}%.')

if __name__ == "__main__":
    print(2**38)