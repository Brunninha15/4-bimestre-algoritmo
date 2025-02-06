numero = []

for i in range(10):
    numerounitario= float(input("digite um valor : "))
    numero.append(numerounitario)

posicao = 0

for i in range(10):

    if numero[posicao] < numero[i]: # se o valor da posição atual for menor que 
#valor da posição atual, entao o valor posicao e substituido
        posicao= i



#Agora que ja temos a posição onde esta o maior valor vamos ver que valor esta la dentro

print (f"O valor maior da lista está na posição {posicao}")
print (f"O valor maior da lista é {numero [posicao]}")