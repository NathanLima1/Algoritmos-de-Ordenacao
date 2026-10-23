import java.io.*;

class GFG {
    static void bubbleSort(int vetor[]){
        int tamanho_vetor = vetor.length;
        int temp;
        
        for(int i = 0; i < tamanho_vetor - 1; i++){
            boolean trocou = false;

            int nao_ordenados = tamanho_vetor - i - 1;

            for(int j = 0; j < tamanho_vetor; j++){
                if(vetor[j] > vetor[j+1]){
                    temp = vetor[j];
                    vetor[j] = vetor[j+1];
                    vetor[j+1] = temp;

                    trocou = true;
                }
            }

            if (trocou == false){
                break;
            }
        }
    }
}