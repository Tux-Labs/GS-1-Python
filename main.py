historicos = []
histcont = 0
plantas = [['Alface', 'T°C: 22°C | Umidade: 60%'], ['Tomate', 'T°C: 22°C | Umidade: 60%'], ['Batata', 'T°C: 22°C | Umidade: 60%']]
div = '-------------------------------------'

def main():
    global histcont
    while True:
        print("====================================")
        print(f"{'PROTOCOLO: Éden':^36s}")
        print("====================================\n")
        print("1. Solução\n2. Estufas\n3. Opção 3\n4. Opção 4\n5. Histórico\n0. Sair")
        print("Digite a opção que você deseja acessar\n")
        op = input("- ")
        if op == '1':
            histcont += 1
            op1()
        elif op == '2':
            histcont += 1
            op2()
        elif op == '3':
            histcont += 1
            op3()
        elif op == '4':
            histcont += 1
            op4()
        elif op == '5':
            op5()
        elif op == '0':
            return
        else:
            print("\nOpção inválida\n")

def op1():
    historicos.append("Solução")
    print(f"{div}\n")
    print("A solução consiste em uma estufa inteligente automatizada capaz de monitorar e controlar variáveis\nessenciais para o cultivo de plantas em Marte\n\nO sistema coleta dados de temperatura e umidade em tempo real e toma decisões automaticamente para\nmanter o ambiente adequado para o desenvolvimento da plantação.\n")
    input("Digite algo para voltar: ")

def op2():
    historicos.append("Estufas")
    while True:
        print(f"{div}\n")
        print("1. Acessar Estufas\n2. Adicionar Estufa\n0. Voltar")
        print("Digite a opção que você deseja acessar\n")
        op = input("- ")
        if op == '1':
            print(f"{div}\n")
            print("Estufas ativas:")
            for planta in plantas:
                print(planta[0])
            print("\n(Digite 0 para retornar)")
            opcao = input("Digite a estufa que deseja visitar: ").lower().capitalize()
            for planta in plantas:
                if planta[0] == opcao:
                    print(f'\n{planta}\n')
                    input("Digite algo para voltar: ")
                elif opcao == '0':
                    break
        elif op == '2':
            print(f'{div}\n')
            novap = input("Digite a cultura que deseja adicionar: ").lower().capitalize()
            plantas.append([novap, 'T°C: 22°C | Umidade: 60%'])
            print(f"Adicionando {novap} ao monitoramento")
        elif op == '0':
            return
        else:
            print("Opção inválida")

def op3():
    historicos.append("Op3")
    print()

def op4():
    historicos.append("Op4")
    print()

def op5():
    global histcont
    print(f"Funções acessadas: {histcont}\nHistórico: {historicos}")
    input("Digite algo para voltar: ")

main()