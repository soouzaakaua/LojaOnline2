while True:
    # Coleta dos dados da avaliação
    nomeFilme = input("Digite o nome do filme: ")
    notaMed = int(input("Qual nota você daria para o filme (de 1 a 10)? "))
    comentario = input("Deixe seu comentário sobre o filme: ")
    faixaetaria = input("O filme é adequado para crianças (sim/não)? ")

    # Impressão dos dados da avaliação
    print("\nAvaliação registrada:")
    print(f"Nome do filme: {nomeFilme}")
    print(f"Nota: {notaMed}")
    print(f"Comentário: {comentario}")
    print(f"Adequado para crianças: {faixaetaria}")

    # Pergunta se deseja adicionar outra avaliação
    continuar = input("\nDeseja adicionar outra avaliação? (s/n): ")
    if continuar.lower() != 's':
        break  # Encerra o loop se a resposta não for 's'

print("Programa encerrado.")