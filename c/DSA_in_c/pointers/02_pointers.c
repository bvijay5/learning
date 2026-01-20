#include<stdio.h>

void swap(int a, int b){
    int t = a;
    a = b;
    b = t;
    printf("\na=%d, b=%d\n", a,b);
}

_swap(int* a, int* b){
    int t = *a;
    *a = *b;
    *b = t;
    
}

int main(){
    int a = 5, b = 10;
    swap(a,b);

    _swap(&a, &b);

}