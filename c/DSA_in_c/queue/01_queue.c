#include <stdio.h>
#define MAX 5

int queue[MAX];
int front = -1, rear = -1;

// Check if queue is empty
int isEmpty() {
    return (front == -1);
}

// Check if queue is full
int isFull() {
    return (rear == MAX - 1);
}

// Enqueue operation
void enqueue(int data) {
    if (isFull()) {
        printf("Queue is full\n");
        return;
    }
    if (front == -1) front = 0; // first element
    queue[++rear] = data;
    printf("%d inserted into queue\n", data);
}

// Dequeue operation
void dequeue() {
    if (isEmpty()) {
        printf("Queue is empty\n");
        return;
    }
    printf("%d removed from queue\n", queue[front]);
    if (front == rear) { // last element removed
        front = rear = -1;
    } else {
        front++;
    }
}

// Peek operation
void peek() {
    if (isEmpty()) {
        printf("Queue is empty\n");
    } else {
        printf("Front element is %d\n", queue[front]);
    }
}

// Display queue
void display() {
    if (isEmpty()) {
        printf("Queue is empty\n");
        return;
    }
    printf("Queue elements: ");
    for (int i = front; i <= rear; i++) {
        printf("%d ", queue[i]); 
    }
    printf("\n");
}

int main() {
    enqueue(10);
    enqueue(20);
    enqueue(30);
    display();
    peek();
    dequeue();
    display();
    return 0;
}
