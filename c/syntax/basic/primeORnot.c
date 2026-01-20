#include<stdio.h>
//check if a number is prime or not
int main(){
    int n,count=0;
    printf("Enter a number: ");
    scanf("%d",&n);

    for(int i=2;i*i<=n;i++){
        if(n%i==0){
            count++;
            break;
        }
    }

    if(count==0){
        printf("%d is a prime number\n",n);
    }
    else{
        printf("%d is not a prime number\n",n);
    }
}