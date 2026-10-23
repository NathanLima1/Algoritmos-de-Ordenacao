#include <stdio.h>
#include <stdbool.h>

void trocar(int* elemento1, int* elemento2){
    /*Função para trocar a ordem de elementos de um vetor*/
    int temp = *elemento1;
    *elemento1 = *elemento2;
    *elemento2 = temp;
}

void bubbleSort(int* vetor, int tamanho_vetor){
    bool trocou = false;

    // Percorre todos os elementos do vetor
    for(int i = 0; i < tamanho_veto-1; i++){

        // Os últimos i elementos já estão ordenados
        int nao_ordenados = tamanho_vetor - i - 1;

        // Percorre os elementos não ordenados do vetor
        for(int j = 0; j < nao_ordenados; j++){
            // Troca as posições se o elemento atual do vetor é maior
            // do que o próximo
            if(vetor[j] > vetor[j+1]){
                trocar(&vetor[j], &vetor[j+1]);
                trocou = true;
            }
        }

        // Se não houve trocas, o vetor já está ordenado
        if(trocou == false){
            break;
        }
    }
}
