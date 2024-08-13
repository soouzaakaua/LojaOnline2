# MENU
print('='*50) 
print(''*7 + 'BEM-VINDO A LOJA DE GELADOS DO KAUÃ SAMUEL') 
print('='*50) 
print('='*2,'|','TAMANHO','|',  'CUPUAÇU (CP)','|','  AÇAI (AC) ','|', '='*2)
print('='*2,'|','   P   ','|',  '   R$9.00   ','|', '   R$11.00   ','|','='*2)
print('='*2,'|','   M   ','|',  '   R$14.00  ','|', '   R$16.00   ','|','='*2)
print('='*2,'|','   G   ','|',  '   R$18.00  ','|', '   R$20.00   ','|','='*2)
print('='*50)

#MENU

# Definindo os preços
precos = {
    'AC': {'P': 11.00, 'M': 16.00, 'G': 20.00},
    'CP': {'P': 9.00, 'M': 14.00, 'G': 18.00}
}

# Inicializando o acumulador para somar os valores dos pedidos
total_pedido = 0

# Loop para fazer pedidos
while True:
    # Input do sabor
    sabor = input('Qual o sabor desejado? (AC/CP): ').upper()
    if sabor not in ['AC', 'CP']:
        print('Sabor inválido. Tente novamente!')
        continue

    # Input do tamanho
    tamanho = input('Qual o tamanho desejado? (P/M/G): ').upper()
    if tamanho not in ['P', 'M', 'G']:
        print('Tamanho inválido. Tente novamente!')
        continue

    # Processando o pedido e acumulando o total
    total_pedido += precos[sabor][tamanho]
    print(f'Você pediu um {sabor} no tamanho {tamanho}. Total até agora: R${total_pedido:.2f}')

    # Pergunta se deseja fazer mais pedidos
    outro_pedido = input('Deseja pedir mais alguma coisa? (SIM/NÃO) ').upper()
    if outro_pedido != 'SIM':
        break

# Exibindo o total do pedido
print(f'Total do pedido: R${total_pedido:.2f}')