#include<stdio.h>

void square(int n){
    n = n*n;
    printf("square of n is :%d\n", n);
}

void _square(int* n){
    *n = (*n)*(*n);
    printf("square of n is :%d\n", *n);
}

int main(){
    int number=5;
    square(number);
    printf("%d\n", number);
    _square(&number);
    printf("%d\n", number);
}