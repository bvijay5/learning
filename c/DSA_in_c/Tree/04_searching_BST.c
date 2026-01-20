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

void inOrder(struct node* root){
    if(root!=NULL){
        inOrder(root->left);
        printf("%d, ", root->data);
        inOrder(root->right);
    }
}

int isBST(struct node* root){
    static struct node* prev = NULL;
    if(root!=NULL){
        if(!isBST(root->left)){
            return 0;
        }
        if(prev!=NULL && root->data <= prev->data){
            return 0;
        }
        prev = root;
        return isBST(root->right);
    }
    else{
        return 1;
    }
}

struct node* searchBST(struct node* root, int key){
    if(root==NULL){
        return NULL;
    }
    if(root->data == key){
        return root;
    }
    else if(key<root->data){
        return searchBST(root->left,key);
    }
    else{
        return searchBST(root->right,key);
    }
}
//Iterative search in BST
struct node* iterativeBST(struct node* root, int key){
    while(root!=NULL){
        if(root->data == key){
            return root;
        }
        else if(key< root->data){
            root = root->left;
        }
        else{
            root = root->right;
        }
    }
    return NULL;
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

    inOrder(root);
    printf("\n");
    printf("%d", isBST(root));
    printf("\n");
    struct node* k = searchBST(root, 7);
    if(k!=NULL){
        printf("Found: %d", k->data);
    }
    else{
        printf("Element not found\n");
    }
}