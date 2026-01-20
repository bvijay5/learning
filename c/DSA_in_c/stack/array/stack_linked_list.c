#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node* next;
};

struct node* top = NULL;

void push(int x){
    struct node* ptr = (struct node*)malloc(sizeof(struct node));
    if(ptr == NULL){
        printf("Stack Overflow\n");
        return;
    }
    ptr->data = x;
    ptr->next = top;
    top = ptr;
    printf("Element pushed to stack: %d\n", x);
}

void pop(){
    if(top == NULL){
        printf("Stack Underflow\n");
        return;
    }
    printf("Element popped: %d\n", top->data);
    struct node* ptr = top;
    top = top->next;
    free(ptr);
}

void display(){
    if(top == NULL){
        printf("Stack is empty\n");
        return;
    }
    struct node* ptr = top;
    while(ptr != NULL){
        printf("%d->", ptr->data);
        ptr = ptr->next;
    }
    printf("NULL\n");
}

int main(){
    push(1);
    push(2);
    pop();
    push(5);
    display();
    
    return 0;
}
