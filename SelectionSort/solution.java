
class GFG{
    static void selectionSort(int vetor[]){
        int tamanho_vetor = vetor.length;

        for(int i = 0; i < tamanho_vetor-1; i++){
            int min_indice = i;

            for(int j = i; j < tamanho_vetor; j++){
                if(vetor[j] < vetor[min_indice]){
                    min_indice = j;
                }
            }

            int temp = vetor[i];
            vetor[i] = vetor[min_indice];
            vetor[min_indice] = temp;
        }
    }
}