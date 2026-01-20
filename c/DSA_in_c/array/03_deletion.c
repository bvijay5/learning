#include <stdio.h>

int main() {
    int arr[100];   // Maximum size of array
    int n, pos;

    // Step 1: Input size of array
    printf("Enter number of elements in array: ");
    scanf("%d", &n);

    // Step 2: Input elements
    printf("Enter %d elements:\n", n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Step 3: Input position to delete
    printf("Enter position to delete (1 to %d): ", n);
    scanf("%d", &pos);

    // Step 4: Check for valid position
    if(pos < 1 || pos > n) {
        printf("Invalid position!\n");
    } else {
        // Step 5: Shift elements to the left
        for(int i = pos - 1; i < n - 1; i++) {
            arr[i] = arr[i + 1];
        }

        n--;  // reduce size after deletion

        // Step 6: Print updated array
        printf("Array after deletion:\n");
        for(int i = 0; i < n; i++) {
            printf("%d ", arr[i]);
        }
        printf("\n");
    }

    return 0;
}
