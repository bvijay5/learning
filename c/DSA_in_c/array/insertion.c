#include <stdio.h>

int main() {
    int arr[100];   // array with maximum size 100
    int n, pos, value;

    // Step 1: Input size of array
    printf("Enter number of elements in array: ");
    scanf("%d", &n);

    // Step 2: Input elements
    printf("Enter %d elements:\n", n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Step 3: Input position and value to insert
    printf("Enter position to insert (1 to %d): ", n+1);
    scanf("%d", &pos);
    printf("Enter value to insert: ");
    scanf("%d", &value);

    // Step 4: Check for valid position
    if(pos < 1 || pos > n+1) {
        printf("Invalid position!\n");
    } else {
        // Step 5: Shift elements to right
        for(int i = n; i >= pos; i--) {
            arr[i] = arr[i-1];
        }

        // Step 6: Insert new element
        arr[pos-1] = value;
        n++;  // increase size

        // Step 7: Print updated array
        printf("Array after insertion:\n");
        for(int i = 0; i < n; i++) {
            printf("%d ", arr[i]);
        }
        printf("\n");
    }

    return 0;
}
