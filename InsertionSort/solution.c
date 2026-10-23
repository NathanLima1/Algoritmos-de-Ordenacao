#include <stdio.h>

void insertionSort(int vetor[], int tamanho_vetor){
    for(int i = 1; i < tamanho_vetor; i++){
        int atual = vetor[i];
        int j = i - 1;

        while(j >= 0 && vetor[j] > atual){
            vetor[j+1] = vetor[j];
            j--;
        }
        vetor[j+1] = atual;
    }
}