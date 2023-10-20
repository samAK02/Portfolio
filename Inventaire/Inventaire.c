#include <stdio.h>
#include <string.h>

typedef struct 
{
    int prix, quantite;
    char nom[12];

} article;


void Trouve(article T[], int N, char nom_Recherche[])
{
    int i, booleen = 0;

    for (i = 0; i < N; i++)
    {
        if (strcmp(T[i].nom, nom_Recherche) == 0)
        {
            printf("Article trouvé: \n nom: %s \n Quantite: %d \n Prix: %d\n", T[i].nom, T[i].quantite, T[i].prix);
            booleen = 1;
        }
    }

    if (booleen == 0)
    {
        printf("Article indisponible.\n");
    }
}

int main() {
    article T[10];
    int i, N;
    char nom_recherche[12];

    printf("Combien d'articles votre magasin possède: ");
    scanf("%d", &N);

    for (i = 0; i < N; i++)
    {
        printf("Entrez le nom de votre article: ");
        scanf("%s", T[i].nom);
        printf("Votre article est: %s\n", T[i].nom);
        printf("Entrez le nombre d'exemplaire de votre produit: ");
        scanf("%d", &T[i].quantite);
        printf("Il existe en: %d\n", T[i].quantite);
        printf("Veuillez entrer le prix de votre produit: ");
        scanf("%d", &T[i].prix);
        printf("Il coute: %d\n", T[i].prix);
    }

    printf("Entrez l'article que vous cherchez: ");
    scanf("%s", nom_recherche);
    Trouve(T, N, nom_recherche);

    return 0;
}