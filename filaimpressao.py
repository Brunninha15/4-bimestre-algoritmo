def menu():
    fila_impressao= FilaDEIpressao()

    fila_impressao.configurar_inicial()

while True:
       print("Opções:")
       print("1. Adicionar um trabalho na fila de impressão.")
       print("2. Imprimir o próximo trabalho na fila.")
       print("3. Mostrar a fila de impressão.")
       print("4. Sair")
       escolha = input("Eacolha uma opção 1-4")
       #Aqui vai ser lido a escolha do usuário
       
if escolha== "1":
    trabalho = input("Digite o nome do trabalho a ser impressão")
    #maquina da pessoa que esta imprimindo 
    fila_impressao.adicionar_trabalho(trabalho)
elif escolha== "2":
     fila_impressao.processar_trabalho()
elif escolha== "3":
         fila_impressao.processar_trabalho()
elif escolha== "4":
    print("Saindo do programa.")
    break
else:
    print("Opção invalida.")