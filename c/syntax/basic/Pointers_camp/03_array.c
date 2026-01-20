#include<stdio.h>

int main(){
    int a[5] = {1,2,3,4,5};
    int* p;
    p = a;
    printf("%d\n", a);          //address of a[0]
    printf("%d\n", &a[0]);      //address of a[0]

    printf("%d\n", a[0]);       //prints first element
    printf("%d\n", *a);         //prints first element

}