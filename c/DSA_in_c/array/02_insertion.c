#include <stdio.h>

int main() {
    int arr[100];   // array with maximum size 100
    int n, value;

    // Step 1: Input size of array
    printf("Enter number of elements in array: ");
    scanf("%d", &n);

    // Step 2: Input elements
    printf("Enter %d elements:\n", n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Step 3: Input value to insert at index 0
    printf("Enter value to insert at index 0: ");
    scanf("%d", &value);

    // Step 4: Shift elements one step right
    for(int i = n; i > 0; i--) {
        arr[i] = arr[i-1];
    }

    // Step 5: Place new value at index 0
    arr[0] = value;
    n++;  // array size increases by 1

    // Step 6: Print updated array
    printf("Array after insertion at index 0:\n");
    for(int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
