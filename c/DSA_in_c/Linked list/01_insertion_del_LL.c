#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node* next;
};

void traversalL(struct node* head){
    while(head!=NULL){
        printf("%d->", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

struct node* addAtFirst(struct node* head, int data){
    struct node* ptr = (struct node*)malloc(sizeof(struct node));
    ptr->data = data;
    ptr->next = head;
    return ptr;
}

struct node* addAtIndex(struct node* head, int data, int index){
    struct node* ptr = (struct node*)malloc(sizeof(struct node));
    ptr->data = data;
    struct node* q = head;
    int i = 0;
    while(i!=index-1){
        q = q->next;
        i++;
    }
    ptr->next = q->next;
    q->next = ptr;
    return head;
}

struct node* addAtLast(struct node* head, int data){
    struct node* ptr = (struct node*)malloc(sizeof(struct node));
    ptr->data = data;
    struct node* q = head;
    while(q->next!=NULL){
        q = q->next;
    }
    q->next = ptr;
    ptr->next = NULL;
    return head;
}

struct node* deleteAtFirst(struct node* head){
    struct node* ptr = head;
    head = head->next;
    free(ptr);
    return head;
}

struct node* deleteAtIndex(struct node* head,int index){
    struct node* ptr = head;
    int i = 0;
    while(i!=index-1){
        ptr = ptr->next;
        i++;
    }
    struct node* q = ptr->next;
    ptr->next = q->next;
    free(q);
    return head;
}

struct node* deleteAtLast(struct node* head){
    struct node* ptr = head;
    struct node* q = ptr->next;
    while(q->next!=NULL){
        ptr = ptr->next;
        q = q->next;
    }
    ptr->next = NULL;
    free(q);
    return head;
}

struct node* deleteValue(struct node* head, int value){
    struct node* ptr = head;
    struct node* q = ptr->next;
    if(ptr->data == value){
        head = head->next;
        free(ptr);
    }
    while(q->data != value && q->next!=NULL){
        ptr = ptr->next;
        q = q->next;
    }
    if(q->data == value){
        ptr->next = q->next;
        free(q);
    }
    return head;
}

int main(){
    struct node* head = (struct node*)malloc(sizeof(struct node));
    struct node* second = (struct node*)malloc(sizeof(struct node));
    struct node* third = (struct node*)malloc(sizeof(struct node));

    head->data = 1;
    head->next = second;

    second->data = 2;
    second->next = third;

    third->data = 3;
    third->next = NULL;

    traversalL(head);
    head = deleteValue(head,12);
    traversalL(head);

    return 0;
}