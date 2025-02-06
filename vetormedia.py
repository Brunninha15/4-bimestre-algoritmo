nota = []

for i in range(5):
  notaunitario = float(input("digite a nota do aluno:"))
  nota.append (notaunitario)

  media = 0
  for no in nota: 
    media = media + no

    media = media/5

    print ("media geral: {media}")