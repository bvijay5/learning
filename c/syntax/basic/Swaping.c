#include <stdio.h>

int main(){
    // Swapping two numbers using a temporary variable
    int a,b,temp;
    printf("Enter two numbers: ");
    scanf("%d %d",&a,&b);
    printf("Before swapping: a = %d, b = %d\n",a,b);
    temp = a;
    a = b;
    b = temp;
    printf("After swapping: a = %d, b = %d\n",a,b);

    // Method 2: Swapping two numbers without using a temporary variable

    // int x,y;
    // printf("Enter two numbers: ");
    // scanf("%d %d",&x,&y);
    // printf("Before swapping: x = %d, y = %d\n",x,y);
    // x = x + y; // Step 1: x now holds the sum of x and y // (CAN EVEN USE * AND /)
    // y = x - y; // Step 2: y is now the original x
    // x = x - y; // Step 3: x is now the original y
    // printf("After swapping: x = %d, y = %d\n",x,y); 

    return 0;
}