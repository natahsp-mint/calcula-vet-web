#include <stdio.h>

int main(){

    float peso, dose;
    int especie;
    char farmaco[50];

    peso = 0;
    dose = 0;

    printf("Bem-vindo a Calcula Vet!\n\n");

    printf("Digite o nome do farmaco, sem acento:\n");
    scanf("%50s", &farmaco);



// START - calculadora simples de meloxicam cao e gato.

            printf("\nSelecione a especie:\n1 - Cao\n2 - Gato\n");
            scanf("%d", &especie);

            printf("\nInsira o peso em kg:\n");
            printf("(Lembre-se de usar ponto, nao virgula)\n");
            scanf("%f", &peso);

                switch(especie) {
                    case 1:
                    dose = 0.1 * peso;
                    printf("\nA dose eh %.2f mg SID\n", dose);
                    break;
                    case 2:
                    dose = 0.05 * peso;
                    printf("\nA dose eh %.2f mg SID\n", dose);
                    break;
                    default:
                    printf("especie invalida.\n")
                }

// END



    return 0;

}
