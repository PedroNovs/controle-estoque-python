estoque = {'parafuso': 70 , 'manta': 160 , 'pneu': 80, 'forro': 95 , 'teto': 150}

#FUNÇÕES ======

def consultar_estoque(estoque):
    print(f'Consultando estoque ...\n{estoque}')

def consultar_item(estoque,nomepecas):
    print(f'Tem:{estoque[(nomepecas)]} unidades')

def retirar_pecas(estoque,nomepecas, qntpecas):
    estoque[(nomepecas)] -= qntpecas

def repor_pecas(estoque,nomepecas, qntpecas):
    estoque[(nomepecas)] += qntpecas

def relatorio(estoque):
    print(f'-------------------RELATORIO FINAL-------------------\n')
    for nome, quantidade in estoque.items():
        print(f'{nome}: {quantidade} unidades')
        if estoque[nome] < 10:
            print(f'ATENÇÃO: Pouco {nome} no estoque')

while True:
    nomepecas = str(input('Nome da peça usada:')).lower().strip()
    if nomepecas == 'stop':
        break
    if nomepecas not in estoque:
        print('Não temos esse item em estoque')
    else:
        consultar_item(estoque,nomepecas)
        operacao = str(input('Deseja retirar ou repor peças?')).lower().strip()
        qntpecas = int(input('Quantidade de peças:'))
        if qntpecas <= 0:
            print('Quantidade inválida')
        elif operacao == 'retirar':
            if qntpecas > estoque[nomepecas]:
                print('Estoque insulficiente')
            else:
                retirar_pecas(estoque,nomepecas,qntpecas)
                print('Peças retirada do estoque')
        elif operacao == 'repor':
            repor_pecas(estoque, nomepecas, qntpecas)
            print('Peças adicionas ao estoque')
        else:
            print('Operação inválida')

    relatorio(estoque)

print('----------------------------PROGRAMA ENCERRADO----------------------------')
consultar_estoque(estoque)

