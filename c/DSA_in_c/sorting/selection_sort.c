# include<stdio.h>

int main(){
    int arr[6] = {2,1,4,5,6,3};

    for(int i = 0; i<6-1; i++){
        int min = i;

        for(int j = i+1; j<6;j++){
            if(arr[min]> arr[j]){
                min = j;
            }
        }
        if(min != i){
            int temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;
        }
    }

    printf("Sorted array\n");
    for(int i = 0; i<6; i++){
        printf("%d\n", arr[i]);
    }
}
