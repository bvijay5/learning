#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node* next;
};

void printnodes(struct node* head){
    struct node* ptr = head;
    printf("%d->", ptr->data);
    ptr = ptr->next;
    while(ptr != head){
        printf("%d->", ptr->data);
        ptr = ptr->next;
    }
    printf("NULL\n");
}

int main(){
    struct node* head = (struct node*)malloc(sizeof(struct node));
    struct node* second = (struct node*)malloc(sizeof(struct node));
    struct node* third = (struct node*)malloc(sizeof(struct node));

    head->data = 5;
    head->next = second;

    second->data = 6;
    second->next = third;

    third->data = 7;
    third->next = head;

    printnodes(head);

    return 0;
}