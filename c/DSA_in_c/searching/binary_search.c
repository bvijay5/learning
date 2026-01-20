#include<stdio.h>

int main(){
    int arr[10] = {1,2,3,4,5,6,7,8,9,10};
    int key = 50;
    int l = 0;
    int r = 9;
    int found = 0;

    while(l<=r){
        int mid = (l+r)/2;
        if(key == arr[mid]){
            printf("Key: %d found at %d\n", key,mid);
            found = 1;
            break;
        }
        else if(key>arr[mid]){
            l = mid+1;
        }
        else{
            r = mid-1;
        }
    }
    if(found ==0){
        printf("Key: %d not present\n", key);
    }
    return 0;
}
