# Programa 1 

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é {num1}")
elif num2 > num1:
    print(f"O maior número é {num2}")
else:
    print("Os números são iguais.")

  
  # programa 2 
  
    import math  

# Programa 2: Raiz quadrada se positivo

num = int(input("Digite um número inteiro para calcular a raiz quadrada: "))

if num >= 0:
    raiz = math.sqrt(num)
    print(f"A raiz quadrada de {num} é {raiz:.2f}")
else:
    print("Número inválido, pois é negativo.")

  
  # programa 3 
  

num = int(input("Digite um número inteiro para verificar se é par ou ímpar: "))

if num % 2 == 0:
    print(f"O número {num} é PAR.")
else:
    print(f"O número {num} é ÍMPAR.")