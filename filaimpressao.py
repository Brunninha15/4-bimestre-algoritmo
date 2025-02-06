class FilaDeImpressao:

    def configurar_inicial(self):
        self.fila= []
#guarda a fila de impressão no vetor fila

    def adicionar_trabalho(self, trabalho):
        self.fila.append(trabalho)
        print("trabalho '{trabalho}' adicionando a fila de impressao")
 
    def processar_trabalho(self):
        if not self.esta_vazia():
            trabalho = self.fila.pop(0) #remove o primeiro da fila 
            print("o trabalho '{trabalho}' está sendo processado")
        else:
            print("a fila esta vazia")

    def mostrar_fila(self):
        if self.esta_vazia():
            print("a fila esta vazia!")
        else:
            print("A fila de impressão:")
            for trabalho in self.fila:
                print(f"-{trabalho}")
           
    def esta_vazia(self):
        return len(self.fila) == 0
        
#funçoes de interaçõe com o ususario
def menu():
    fila_impressao= FilaDeImpressao()

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
            fila_impressao.mostrar_fila()
        elif escolha== "4":
            print("Saindo do programa")
            break
        else:
            print("Opção invalida.")


menu()