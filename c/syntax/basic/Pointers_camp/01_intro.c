#include<stdio.h>

int main(){
    int a;
    int *p;
    a = 1025;
    p = &a;
    printf("%d\n", p);
    printf("%d\n", &a);
    printf("%d\n",*p);

    char *po;
    // po = p;
    // printf("%d\n", po); //Error(beacuse it has address of interger)
    po = (char*)p;
    printf("%d\n",p);
    printf("%d\n", *po);
}