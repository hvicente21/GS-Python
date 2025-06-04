#Henrique Vicente RM:564116
#Arthur Gil RM:555746
#Matheus Cerciari RM:565817


# --- Listas para armazenar os dados do sistema ---
areas_de_risco = []
registros_trafego = []
contribuicoes_cidadao = []


# --- Funções para cada funcionalidade ---

def consultar_previsao_alagamento():
    # Solicita a entrada de dados do usuário
    area = input("Digite a area que sera classificada: ")
    while area == "":
        area = input("Digite a area que sera classificada: ")

    nivelPrecipitação = input("Digite o nivel de precipitação em mm/h: ")
    while not nivelPrecipitação.isnumeric():
        print("Invalido")
        nivelPrecipitação = input("Digite o nivel de precipitação em mm/h: ")
    nivelPrecipitação = int(nivelPrecipitação)

    umidadeSolo = input("Digite a umidade do solo em %: ")
    while not umidadeSolo.isnumeric():
        print("Invalido")
        umidadeSolo = input("Digite a umidade do solo em %: ")
    umidadeSolo = int(umidadeSolo)

    # Lógica de classificação
    if nivelPrecipitação > 60 and umidadeSolo > 90:
        nivelRisco = "Crítico"
        statusAlagamento = "Alagado"
    elif nivelPrecipitação > 30 and umidadeSolo > 70:
        nivelRisco = "Alto"
        statusAlagamento = "Em Observação"
    elif nivelPrecipitação > 10 and umidadeSolo > 50:
        nivelRisco = "Moderado"
        statusAlagamento = "Seco (com potencial)"
    else:
        nivelRisco = "Baixo"
        statusAlagamento = "Seco"

    # Adiciona a área e o nível de risco à lista
    areas_de_risco.append((area, nivelRisco)) # Armazena em minúsculas para padronizar

    print("\n--- Resultado da Classificação ---")
    print(f"Para a Área {area}:")
    print(f"  Nível de Risco: {nivelRisco}")
    print(f"  Status de Alagamento: {statusAlagamento}")


def registrar_trafego():
    """ 
    Permite ao usuário registrar o estado do tráfego para uma rua. 
    """
    print("\n--- Registrar Tráfego ---")
    nome_rua = input("Digite o nome da rua: ")
    estado = input("Digite o estado do tráfego (livre, lento, parado): ")

    # Validação simples do estado do tráfego
    if estado in ["livre", "lento", "parado"]:
        registros_trafego.append((nome_rua, estado))
        print(f"Tráfego para '{nome_rua}' registrado como '{estado}'.")
    else:
        print("Estado de tráfego inválido. Use 'livre', 'lento' ou 'parado'.")


def sugerir_rota_basica():
    """ 
    Sugere uma rota básica com base nos dados simplificados. 
    É uma simulação bem simples, sem lógica de caminho real. 
    """
    print("\n--- Sugerir Rota (Básica) ---")
    origem = input("Digite o ponto de partida: ")
    destino = input("Digite o ponto de destino: ")

    print(f"\nSugestão de rota de '{origem}' para '{destino}':")

    # Verifica se há alguma área de alto risco cadastrada
    risco_alto_presente = False
    for _, nivel in areas_de_risco:
        if nivel == "alto":
            risco_alto_presente = True
            break

    # Verifica se há alguma rua com tráfego parado
    trafego_parado_presente = False
    for _, estado in registros_trafego:
        if estado == "parado":
            trafego_parado_presente = True
            break

    if risco_alto_presente or trafego_parado_presente:
        print("Atenção: A rota pode passar por áreas de alto risco de alagamento ou tráfego parado.")
        print("Recomenda-se cautela ou buscar rotas alternativas.")
    else:
        print("A rota parece segura, sem grandes riscos de alagamento ou tráfego intenso reportados.")


def simular_envio_alerta():
    """ 
    Simula o envio de um alerta para grupos de usuários. 
    """
    print("\n--- Simular Envio de Alerta ---")
    mensagem = input("Digite a mensagem do alerta: ")
    grupos = input("Para quais grupos enviar (todos, grupo A, grupo B - separados por vírgula): ")

    lista_grupos = grupos.split(',')

    print("\n--- Alerta Simulado ---")
    print(f"Mensagem: '{mensagem}'")
    print(f"Enviado para: {', '.join(lista_grupos)}")
    print("Alerta enviado (simulação)!")


def contribuir_cidadao():
    """ 
    Permite ao cidadão enviar uma contribuição em texto. 
    """
    print("\n--- Contribuição Cidadã ---")
    contribuicao = input("Descreva a condição local (ex: 'Rua X com água no joelho'): ")
    contribuicoes_cidadao.append(contribuicao)
    print("Sua contribuição foi registrada. Obrigado!")


def painel_de_dados_simples():
    """ 
    Exibe um painel simples com um resumo dos dados. 
    """
    print("\n--- Painel de Dados Simples ---")
    print(f"Total de Áreas de Risco Classificadas: {len(areas_de_risco)}")
    print(f"Total de Registros de Tráfego: {len(registros_trafego)}")
    print(f"Total de Contribuições Cidadãs: {len(contribuicoes_cidadao)}")


    # Exibir ruas com tráfego parado
    print("\n--- Ruas com Tráfego Parado ---")
    trafego_parado_encontrado = False
    for rua, estado in registros_trafego:
        if estado == "parado":
            print(f"- {rua}")
            trafego_parado_encontrado = True
    if not trafego_parado_encontrado:
        print("Nenhuma rua com tráfego parado registrada.")

    # Exibir últimas contribuições
    print("\n--- Últimas Contribuições Cidadãs ---")
    if len(contribuicoes_cidadao) > 0:
        for i in range(max(0, len(contribuicoes_cidadao) - 3), len(contribuicoes_cidadao)):
            print(f"- {contribuicoes_cidadao[i]}")
    else:
        print("Nenhuma contribuição cidadã registrada.")


# --- Menu Principal do Programa ---

def exibir_menu():
    """ 
    Exibe o menu de opções para o usuário. 
    """
    print("\n==== Sistema de Monitoramento Urbano (Básico) ====")
    print("1. Consultar Previsão de Alagamento")
    print("2. Registrar Tráfego")
    print("3. Sugerir Rota (Básica)")
    print("4. Simular Envio de Alerta")
    print("5. Contribuição Cidadã")
    print("6. Painel de Dados Simples")
    print("7. Sair")
    print("==================================================")


def main():
    """ 
    Função principal que gerencia o fluxo do programa. 
    """
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            consultar_previsao_alagamento()
        elif escolha == '2':
            registrar_trafego()
        elif escolha == '3':
            sugerir_rota_basica()
        elif escolha == '4':
            simular_envio_alerta()
        elif escolha == '5':
            contribuir_cidadao()
        elif escolha == '6':
            painel_de_dados_simples()
        elif escolha == '7':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 7.")


# --- Inicia o programa ---
if __name__ == "__main__":
    main()