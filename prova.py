import random
def lancar_dados(d1,d2):
    d1 = random.randint(1,6)
    soma=d1+d2
    return soma

d1 = random.randint(1,6)
print(f'Valor do 1° dado: {d1}')
d2 = random.randint(1,6)
print(f'Valor do 2° dado: {d2}')
print(f' A soma dos dados é {lancar_dados(d1,d2)}')