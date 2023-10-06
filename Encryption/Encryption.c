#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *input, *output;
    char lettre;

    input = fopen("data.txt", "r");
    if(input == NULL){
        puts("Erreur: Impossible d'ouvrir le fichier.");
        exit(1);
    }

    output = fopen("Ouput.txt", "w");
    while((lettre = fgetc(input)) != EOF){
        if(lettre <= 'a' && lettre <= 'z'){
            lettre = ((lettre - 'a')+4) *2;
        }
        else if(lettre >='A' && lettre <= 'Z'){
            lettre = ((lettre - 'A')+4) * 2;
        }
        fputc(lettre, output);
    }

    printf("Encryption terminée.\n");
    printf("Output.exe est crée");

    fclose(input);
    fclose(output);
    return 0;
}
