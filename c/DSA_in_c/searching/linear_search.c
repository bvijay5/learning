#include<stdio.h>

int main(){
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    
    int arr[n];

    printf("\nEnter the elements: \n");
    for(int i = 0; i<n; i++){
        scanf("%d", &arr[i]);
    }

    int s;
    printf("Enter the value to search: ");
    scanf("%d", &s);

    int found = 0;
    for(int i = 0; i<n; i++){
        if(arr[i]==s){
            printf("\nElement %d found at index %d.\n", s,i);
            found = 1;
            break;
        }
    }
    if(found == 0){
        printf("\nElement not present in array.\n");
    }
}