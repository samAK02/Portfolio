#include<stdio.h>
#include<stdlib.h>

typedef struct node {
    int data;
    struct node* next;
} node;

void Ajout(node** head, int data) {
    node* new_node = (node*)malloc(sizeof(node));
    new_node->data = data;
    new_node->next = NULL;

    if (*head == NULL) {
        *head = new_node;
    }
    else {
        node* curr = *head;
        while (curr->next != NULL) {
            curr = curr->next;
        }
        curr->next = new_node;
    }
}

void Affiche(node* head) {
    if (head == NULL) {
        printf("liste vide.\n");
    }
    else {
        printf("Votre liste:\n");
        while (head != NULL) {
            printf("%d\n", head->data);
            head = head->next;
        }
    }
}

int main() {
    node* head = NULL;
    int N, i, data;

    do {
        printf("Combien d'éléments voulez-vous insérer? ");
        scanf("%d", &N);
    } while (N < 0);

    printf("Insérez votre data:\n");

    for (i = 0; i < N; i++) {
        printf("Donnée n°%d: ", i + 1);
        scanf("%d", &data);
        Ajout(&head, data);
    }
    Affiche(head);

    return 0;
}