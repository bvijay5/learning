#include<stdio.h>

int main(){
    int arr[5] = {2,1,4,5,3};

    for(int i = 1; i<5; i++){
        for(int j=0; j<5-i;j++){
            if(arr[j]>arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    printf("\nArray: \n");
    for(int i = 0; i<5; i++){
        printf("%d\n", arr[i]);
    }
}
