def mostrarNumero()
  numero_valido = False

while(numero_valido == False):
  try:
    num = int(input())
    if(num > 100):
      print("O numero precisa ser menor ou igual a 100")
    else:
      print("Boa! Voce escolheu o número: " + str(num))
      numero_valido = True
   except:
    print("Precisa digitar um numero inteiro") 
mostrarNumero()      

