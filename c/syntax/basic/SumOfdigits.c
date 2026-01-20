#include<stdio.h>
//Count the sum of a number(1234=10)

int main(){
    int n,r, sum = 0;
    printf("Enter a number: ");
    scanf("%d", &n);

    while(n>0){
        r = n%10;
        sum+=r;
        n = n/10;
    }

    printf("Sum of digits of a numbers is: %d\n", sum);
}