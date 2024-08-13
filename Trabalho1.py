#MENU 

print('='*31) 
print(''*7 + 'BEM-VINDO A LOJA DO KAUÃ SAMUEL') 
print('='*31) 

#MENU 

vln = float(input('qual o valor unitário? ')) 
qtd = float(input('quantas unidades? ')) 
valor_final = vln * qtd 

if(valor_final < 2500): 

    desc = valor_final * 0/100 # calculo do valor de desconto 
    vldescont = valor_final - desc 
    print(f'O valor total é = R${valor_final}\nNenhum desconto disponivel!') 

elif(valor_final >= 2500 and valor_final < 6000): 
    desc = valor_final * 4/100 # calculo do valor de desconto 
    vldescont = valor_final - desc 
    print(f'O valor total é = R${valor_final}\nCom desconto se tornou = R${vldescont}')   
    
elif(valor_final >= 6000 and valor_final < 10000): 
    desc = valor_final * 7/100 # calculo do valor de desconto 
    vldescont = valor_final - desc 
    print(f'O valor total é = R${valor_final}\nCom desconto se tornou = R${vldescont}') 
     
elif(valor_final >= 10000): 
    desc = valor_final * 11/100 # calculo do valor de desconto 
    vldescont = valor_final - desc 
    print(f'O valor total é = R${valor_final}.\nCom desconto se tornou = R${vldescont}')   
else: 
      print('HOUVE ALGUM ERRO!') 