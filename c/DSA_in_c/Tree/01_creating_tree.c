#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node* left;
    struct node* right;
};

struct node* createNode(int data){
    struct node* ptr = (struct node*)malloc(sizeof(struct node));
    ptr->data = data;
    ptr->right = NULL;
    ptr->left = NULL;
    return ptr;
}

int main(){
    struct node* root = createNode(5);
    struct node* p1 = createNode(4);
    struct node* p2 = createNode(3);

    root->right = p2;
    root->left = p1;

    return 0;
}