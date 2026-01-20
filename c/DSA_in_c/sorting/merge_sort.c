// Merge sort(without using functions)

#include <stdio.h>
int main() {
    int n;
    printf("Enter the size of array: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter the elements of array:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Merge Sort
    int temp[n]; // Temporary array for merging

    for (int curr_size = 1; curr_size <= n - 1; curr_size = 2 * curr_size) {
        for (int left_start = 0; left_start < n - 1; left_start += 2 * curr_size) {
            int mid = left_start + curr_size - 1;
            int right_end = (left_start + 2 * curr_size - 1 < n - 1) ? (left_start + 2 * curr_size - 1) : (n - 1);

            // Merging two subarrays
            int i = left_start; // Starting index of left subarray
            int j = mid + 1;   // Starting index of right subarray
            int k = left_start; // Starting index of to be merged subarray

            while (i <= mid && j <= right_end) {
                if (arr[i] <= arr[j]) {
                    temp[k++] = arr[i++];
                } else {
                    temp[k++] = arr[j++];
                }
            }

            while (i <= mid) {
                temp[k++] = arr[i++];
            }

            while (j <= right_end) {
                temp[k++] = arr[j++];
            }

            for (i = left_start; i <= right_end; i++) {
                arr[i] = temp[i];
            }
        }
    }

    printf("Sorted Array:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
