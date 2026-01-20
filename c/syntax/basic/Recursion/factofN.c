#include<stdio.h>
int factN(int n);

int main(){
    printf("%d\n",factN(5));
}

int factN(int n){
    if(n==1){
        return 1;
    }
    return n*factN(n-1); 
}