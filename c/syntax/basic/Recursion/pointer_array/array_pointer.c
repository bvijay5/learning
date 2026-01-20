// int arr1[5];
// int *ptr = &arr1[0];// is same as next line
// int *ptr = arr1;//same as previous line



//eg

#include<stdio.h>

int main(){
    int aadhar[5];


    int *ptr = aadhar;
    for(int i = 0;i<5;i++){
        printf("%d", (ptr+i));
        *ptr++;
    }
}

