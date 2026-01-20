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
    ptr->left = NULL;
    ptr->right = NULL;
    return ptr;
}

int isBST(struct node* root){
    struct node* prev = NULL;
    if(root!=NULL){
        if(!isBST(root->left)){
            return 0;
        }
        if(prev!=NULL && root->data <= prev){
            return 0;
        }
        prev = root;
        return isBST(root->right);
    }
    else{
        return 1;
    }
}

void insert(struct node* root, int data){
    struct node* prev = NULL;
    struct node* trav = root;
    while(trav!=NULL){
        prev = trav;
        if(trav->data == data){
            printf("Element already exist\n");
            return;
        }
        else if(data<trav->data){
            trav = trav->left;
        }
        else{
            trav = trav->right;
        }
    }
    struct node* ptr = createNode(data);
    if(prev->data > data){
        prev->left = ptr;
    }
    else{
        prev->right = ptr;
    }
}

int main(){
    struct node* root = createNode(5);
    struct node* p1 = createNode(3);
    struct node* p2 = createNode(6);
    struct node* p3 = createNode(1);
    struct node* p4 = createNode(4);

    root->left = p1;
    root->right = p2;

    p1->left = p3;
    p1->right = p4;


}
