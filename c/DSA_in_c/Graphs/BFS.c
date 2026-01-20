#include <stdio.h>
#define SIZE 10

// Queue variables
int queue[SIZE];
int front = -1, rear = -1;

// Queue functions
void enqueue(int value) {
    if (rear == SIZE - 1) {
        return; // Queue full
    }
    if (front == -1) {
        front = 0;
    }
    queue[++rear] = value;
}

int dequeue() {
    if (front == -1 || front > rear) {
        return -1; // Queue empty
    }
    return queue[front++];
}

int isEmpty() {
    return (front == -1 || front > rear);
}

int main() {

    int i = 1; // Starting node

    int visited[7] = {0,0,0,0,0,0,0};

    int a[7][7] = {
        {0,1,1,1,0,0,0},
        {1,0,1,0,0,0,0},
        {1,1,0,1,1,0,0},
        {1,0,1,0,1,0,0},
        {0,0,1,1,0,1,1},
        {0,0,0,0,1,0,0},
        {0,0,0,0,1,0,0}
    };

    // Start BFS
    printf("%d ", i);
    visited[i] = 1;
    enqueue(i);

    // BFS traversal
    while (!isEmpty()) {

        int node = dequeue();

        for (int j = 0; j < 7; j++) {
            if (a[node][j] == 1 && visited[j] == 0) {

                printf("%d ", j);
                visited[j] = 1;
                enqueue(j);
            }
        }
    }

    return 0;
}
