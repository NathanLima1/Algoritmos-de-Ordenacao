def bubble_sort(lista):
    tamanho_lista = len(lista)

    # Percorremos todos os elementos da lista
    for i in range(tamanho_lista):
        # Inicialmente consideramos que não é preciso trocar os 
        # elementos de posição
        trocou = False

        # Os últimos i elementos já estão ordenados
        nao_ordenados = tamanho_lista - i - 1

        # Percorre os elementos não ordenados desde o início
        for j in range(0, nao_ordenados):
            # Troca as posições na lista se o elemento atual é maior do que
            # o próximo
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True

        # se não trocou, a lista já está ordenada
        if trocou == False:
            break

