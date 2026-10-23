def selection_sort(lista):
    tamanho_lista = len(lista)

    # Percorre toda a lista com exceção do último elemento
    for i in range(tamanho_lista-1):
        # Considera o primeiro elemento como menor inicial
        min_indice = i

        # Compara com todos os outros elementos a frente se ele é o menor
        for j in range(i+1, tamanho_lista):
            # Se encontra um menor, reconsidera quem é o menor que não foi ordenado
            if lista[j] < lista[min_indice]:
                min_indice = j

        # Coloca o menor elemento encontrado na sua posição correta
        lista[i], lista[min_indice] = lista[min_indice], lista[i]