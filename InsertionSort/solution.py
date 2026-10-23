def insertion_sort(lista):
    tamanho_lista = len(lista)

    for i in range(1, tamanho_lista):
        # Definimos o elemento que vai ser comparado com os outros
        atual = lista[i]
        j = i - 1

        # Enquanto j for um índice válido e o elemento anterior
        # for maior do que o elemento que estamos analisando atualmente
        while j >= 0 and lista[j] > atual:
            # Passamos o elemento que se provou maior 
            # para uma posição a frente na lista
            lista[j+1] = lista[j]
            j -= 1

        # Colocamos o elemento que estavamos analisando 
        # na sua posição correta (atualmente)
        lista[j+1] = atual