#Sistema De Serviços De Cobrança De Uma Copidadora
print('Bem-vindo a Copiadora de Miguel Silveira')
#Escolha De Serviço
def escolha_servico():
    while True:
        print('Escolha o serviço desejado: ')
        print('      |Serviços|       ')
        print('|---------------------------------|')
        print('|DIG -    DIGITALIZAÇÃO           |')
        print('|ICO -    IMPRESSÃO COLORIDA      |')
        print('|IPB -    IMPRESSÃO PRETO E BRANCO|')
        print('|FOT -    FOTOCÓPIA               |')
        print('|---------------------------------|')
        servico=input('\nDigite o serviço que deseja (DIG/ICO/IPB/FOT): ').upper()
        #Preços
        if servico=='DIG':
            return 1.10
        elif servico=='ICO':
            return 1.0
        elif servico=='IPB':
            return 0.40
        elif servico=='FOT':
            return 0.20
        else:
            print('Serviço inválido. Tente novamente.')
            continue
#Número De Páginas
def numero_paginas():
    while True:
        paginas=int(input('\nDigite o número de páginas para a realização do serviço escolhido: '))
        if paginas>=20000:
            print('Número de páginas superior ao permitido. Permitido: 19999. \nTente novamente.')
            continue
        elif 20<= paginas <200:
            return paginas
        elif 200<= paginas <2000:
            return paginas*0.85
        elif 2000<= paginas <20000:
            return paginas*0.75
#Serviço Extra
def servico_extra():
    while True:
        print('\nDeseja um serviço extra ?')
        print('|-------------Serviços-------------|')
        print('| Opções |----|     Serviço        |')
        print('|    1   |----|Encardenação simples|')
        print('|    2   |----|  Encardenação dura |')
        print('|    0   |----|    Mais nada       |')
        extra=int(input('\nDigite o número da opção desejada (1/2/0): '))
        if extra==1:
            return 15.00
        elif extra==2:
            return 40.00
        elif extra==0:
            return 0
        else:
            print('Opção inválida. Tente novamente.')
#Tranformar
valor_serv=escolha_servico()
valor_pag=numero_paginas()
valor_ext=servico_extra()
#Total
total=(valor_serv*valor_pag)+valor_ext
#Programa Completo
print('|---------------Pedido-----------------------|')
print(f'Valor por página (serviço):R${valor_serv:.2f}')
print(f'Valor das páginas (com desconto): R${valor_pag:.2f}')
print(f'Valor do serviço extra :R${valor_ext:.2f}')
print(f'Total a pagar: R${total:.2f}')