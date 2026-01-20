#include<stdio.h>

int main(){
    int arr[6] = {2,1,4,5,6,3};

    for(int i = 1; i<6; i++){
        int temp = arr[i];
        int j = i-1;
        while(j>=0 && arr[j]>temp){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = temp;
    }

    printf("Sorted array\n");
    for(int i = 0; i<6;i++){
        printf("%d\n", arr[i]);
    }
    return 0;
}
