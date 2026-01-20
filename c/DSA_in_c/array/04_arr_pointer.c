#include <stdio.h>

int main() {
    // 1. Declare and initialize an array
    int arr[5] = {10, 20, 30, 40, 50};

    // 2. Pointer to the first element of the array
    int *ptr = arr;  // or int *ptr = &arr[0];

    printf("Accessing array elements using array name:\n");
    for(int i = 0; i < 5; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    printf("\nAccessing array elements using pointer:\n");
    for(int i = 0; i < 5; i++) {
        printf("*(ptr + %d) = %d\n", i, *(ptr + i));
    }

    printf("\nAccessing array elements using pointer increment:\n");
    for(int i = 0; i < 5; i++) {
        printf("Value at ptr = %d\n", *ptr);
        ptr++;  // move pointer to next element
    }

    return 0;

// int main() {
//     int arr[5] = {10, 20, 30, 40, 50};

//     printf("arr       = %p\n", arr);    // address of first element
//     printf("&arr[0]   = %p\n", &arr[0]); // same address
//     printf("*arr      = %d\n", *arr);   // value at arr[0], i.e., 10
//     printf("arr[0]    = %d\n", arr[0]); // also 10

// arr       = 0x7ffee8357a60
// &arr[0]   = 0x7ffee8357a60
// *arr      = 10
// arr[0]    = 10

}
