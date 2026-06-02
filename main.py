historicos = []
histcont = 0
plantas = [['Alface', 'T°C: 22°C | Umidade: 60%', '2 meses', 20], ['Tomate', 'T°C: 21°C | Umidade: 75%', '4 meses', 15], ['Batata', 'T°C: 17°C | Umidade: 85%', '4 meses', 10]]
div = '-------------------------------------'

def main(histcont, plantas):
    while True:
        print("====================================")
        print(f"{'PROTOCOLO: Éden':^36s}")
        print("====================================\n")
        print("1. Solução\n2. Estufas\n3. Almoxarifado\n4. Monitoramento Automático\n5. Histórico\n0. Sair")
        print("Digite a opção que você deseja acessar\n")
        op = input("- ")
        if op == '1':
            historicos.append("Solução")
            histcont += 1
            op1()
        elif op == '2':
            historicos.append("Estufas")
            histcont += 1
            op2(plantas)
        elif op == '3':
            historicos.append("Almoxarifado")
            histcont += 1
            op3(plantas)
        elif op == '4':
            historicos.append("Monitoramento Automático")
            histcont += 1
            op4(plantas)
        elif op == '5':
            op5(histcont)
        elif op == '0':
            return
        else:
            print("\nOpção inválida\n")

def op1():
    print(f"{div}\n")
    print("A solução consiste em uma estufa inteligente automatizada capaz de monitorar e controlar variáveis\nessenciais para o cultivo de plantas em Marte\n\nO sistema coleta dados de temperatura e umidade em tempo real e toma decisões automaticamente para\nmanter o ambiente adequado para o desenvolvimento da plantação.\n")
    input("Digite algo para voltar: ")

def op2(plantas):
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
                    print(div)
                    print(f"\nCultura: {planta[0]}")
                    print(f"Condições ideais: {planta[1]}")
                    print(f"Previsão de colheita: {planta[2]}\n")
                    input("Digite algo para voltar: ")
                elif opcao == '0':
                    break

        elif op == '2':
            print(f'{div}\n')
            novap = input("Digite a cultura que deseja adicionar: ").lower().capitalize()
            temp = int(input("Digite a temperatura ideal (10->99°C): "))
            umi = int(input("Digite a umidade ideal (10->99%): "))
            colheita = input("Digite a previsão de colheita (meses): ")
            if temp < 10 or temp >= 100:
                print("Temperatura inválida")
            elif umi < 10 or umi >= 100:
                print("Umidade inválida")
            else:
                plantas.append([novap, f'T°C: {temp}°C | Umidade: {umi}%', f'{colheita} meses', 0])
                print(f"Adicionando {novap} ao monitoramento")

        elif op == '0':
            return
        
        else:
            print("Opção inválida")

def op3(plantas):
    while True:
        print(f"{div}\n")
        print("ALMOXARIFADO DE SEMENTES")
        print("1. Ver sementes disponíveis")
        print("2. Adicionar sementes")
        print("3. Usar semente")
        print("0. Voltar")
        print("Digite a opção que você deseja acessar\n")

        op = input("- ")

        if op == '1':
            print(f"{div}\n")
            print("Sementes disponíveis:")
            for planta in plantas:
                print(f"{planta[0]} - {planta[3]} unidades")
            input("\nDigite algo para voltar: ")

        elif op == '2':
            nome = input("Digite o nome da semente: ").lower().capitalize()
            qtd = int(input("Digite a quantidade: "))

            encontrou = False

            for planta in plantas:
                if planta[0] == nome:
                    planta[3] += qtd
                    encontrou = True
                    print(f"{qtd} sementes de {nome} adicionadas.")

            if encontrou == False:
                print(div)
                print("Estufa ainda não adicionada\n")
                temp = int(input("Digite a temperatura ideal (10->99°C): "))
                umi = int(input("Digite a umidade ideal (10->99%): "))
                colheita = input("Digite a previsão de colheita (meses): ")
                if temp < 10 or temp >= 100:
                    print("Temperatura inválida")
                elif umi < 10 or umi >= 100:
                    print("Umidade inválida")
                else:
                    plantas.append([nome, f'T°C: {temp}°C | Umidade: {umi}%', f'{colheita} meses', qtd])
                    print(f"Adicionando {nome} ao monitoramento")

        elif op == '3':
            nome = input("Digite a semente que deseja usar: ").lower().capitalize()

            encontrou = False

            for planta in plantas:
                if planta[0] == nome:
                    encontrou = True

                    if planta[3] > 0:
                        planta[3] -= 1
                        print(f"Uma semente de {nome} foi enviada para a estufa.")
                    else:
                        print("Não há sementes disponíveis.")

            if encontrou == False:
                print("Semente não encontrada.")

            input("\nDigite algo para voltar: ")

        elif op == '0':
            return

        else:
            print("Opção inválida")

def op4(plantas):
    print(f"{div}\n")
    print("MONITORAMENTO AUTOMÁTICO DA ESTUFA\n")

    print("Estufas disponíveis:")
    for planta in plantas:
        print(planta[0])

    opcao = input("\nDigite a estufa que deseja monitorar: ").lower().capitalize()

    encontrou = False

    for planta in plantas:
        if planta[0] == opcao:
            encontrou = True

            print(f"\nCultura: {planta[0]}")
            print(f"Condições ideais: {planta[1]}")
            print(f"Previsão de colheita: {planta[2]}")

            temp_atual = int(input("\nDigite a temperatura atual da estufa (°C): "))
            umi_atual = int(input("Digite a umidade atual da estufa (%): "))

            temp_ideal = int(planta[1][5:7])
            umi_ideal = int(planta[1][21:23])

            print(f"\nTemperatura atual: {temp_atual}°C")
            print(f"Temperatura ideal: {temp_ideal}°C")

            if temp_atual < temp_ideal:
                print(">> Temperatura baixa. Aquecendo ambiente...")
            elif temp_atual > temp_ideal:
                print(">> Temperatura alta. Refrigerando ambiente...")
            else:
                print(">> Temperatura ideal.")

            print(f"\nUmidade atual: {umi_atual}%")
            print(f"Umidade ideal: {umi_ideal}%")

            if umi_atual < umi_ideal:
                print(">> Umidade baixa. Irrigando solo...")
            elif umi_atual > umi_ideal:
                print(">> Umidade alta. Reduzindo irrigação...")
            else:
                print(">> Umidade ideal.")

            if temp_atual == temp_ideal and umi_atual == umi_ideal:
                print(f"\nAmbiente ideal para {planta[0]}")
                print(f"A colheita ocorrerá em {planta[2]}")
            else:
                print("\nSistema ajustando a estufa para os parâmetros ideais da cultura.")
            input("\nDigite algo para voltar: ")

    if encontrou == False:
        print("Estufa indisponível.")
        input("Digite algo para voltar: ")

def op5(histcont):
    print(f"{div}\n")
    print(f"Funções acessadas: {histcont}\nHistórico: {historicos}")
    input("Digite algo para voltar: ")

main(histcont, plantas)