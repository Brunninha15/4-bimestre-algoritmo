numero = []
 
for i in range(10):
    numerounitaria = float(input("Digite um numero:"))
    numero.append(numerounitaria)
    
quantidades_negativos= 0
soma_positivos=0
    
for numerounitaria in numero:
    if numerounitaria <0:
        quantidades_negativos +=1
    if numerounitaria > 0:
        soma_positivos += numerounitaria
print(f"quantidade de numeros negativos é: {quantidades_negativos}, e a soma dos positivos é:{soma_positivos} ")
 