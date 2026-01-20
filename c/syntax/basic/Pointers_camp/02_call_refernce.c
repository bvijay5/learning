#include<stdio.h>

void increment(int *p){
    *p = *p+1;
}

int main(){
    int a;
    a = 5;
    increment(&a);
    printf("%d\n",a);
}