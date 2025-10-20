nomes_das_cidades = ['Salvador', 'Fortaleza', 'Natal', 'Aracaju']
distancia = [850, 800, 300, 550]
passeios_e_alimentacao = [200, 400, 250, 300]


def gasto_hotel():
    global dias_de_hospedagem
    return dias_de_hospedagem * 150


def gasto_gasolina():
    global cidade_destino
    return (distancia[cidade_destino] / 14) * 5


def gasto_passeio():
    global cidade_destino, dias_de_hospedagem
    return dias_de_hospedagem * passeios_e_alimentacao[cidade_destino]


while True:
    print('''
    🇶​​​​​🇺​​​​​🇦​​​​​🇳​​​​​🇹​​​​​🇴​​​​​ 🇨​​​​​🇺​​​​​🇸​​​​​🇹​​​​​🇦​​​​​ 🇨​​​​​🇭​​​​​🇪​​​​​🇬​​​​​🇦​​​​​🇷​​​​​ 🇱​​​​​🇦​​​​​́
    ''')
    print('''
    1 - Calcular
    2 - Finalizar
    ''')

    opcao_menu = int(input('Digite 1 para calcular os custos da viagem ou 2 para finalizar: '))

    if opcao_menu == 1:
        while True:
            print('''
            ⓒⓘⓓⓐⓓⓔⓢ
            0 - Salvador
            1 - Fortaleza
            2 - Natal
            3 - Aracaju
            ''')

            cidade_destino = int(input('Informe a cidade que você deseja viajar: '))
            dias_de_hospedagem = int(input('Informe quantos dias você vai passar na cidade: '))

            # validação de entrada
            if 0 <= cidade_destino <= 3 and dias_de_hospedagem > 0:
                custo_total = gasto_hotel() + gasto_gasolina() + gasto_passeio()
                print(f"\nCom base nos gastos definidos, uma viagem de {dias_de_hospedagem} dias para {nomes_das_cidades[cidade_destino]} saindo de Recife custaria aproximadamente R${custo_total:.2f}.\n")
                break  # sai do loop de entrada
            else:
                print('\nPrezado usuário, você digitou um código de cidade inválido ou informou uma quantidade de dias menor que 1.\n')
                print('Tente novamente...\n')

    elif opcao_menu == 2:
        print('Finalizando...')
        break

    else:
        print('Favor selecionar uma opção válida.')
