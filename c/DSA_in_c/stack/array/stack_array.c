#include <stdio.h>
#define MAX 5   // maximum size of stack

int stack[MAX];
int top = -1;  // initially stack is empty

// Check if stack is full
int isFull() {
    return top == MAX - 1;   // returns 1 if full, 0 otherwise
}

// Check if stack is empty
int isEmpty() {
    return top == -1;        // returns 1 if empty, 0 otherwise
}

// Push operation
void push(int x) {
    if (isFull()) {
        printf("Stack Overflow\n");
    } else {
        stack[++top] = x;
        printf("%d pushed to stack\n", x);
    }
}

// Pop operation
void pop() {
    if (isEmpty()) {
        printf("Stack Underflow\n");
    } else {
        printf("%d popped from stack\n", stack[top--]);
    }
}

// Peek operation
void peek() {
    if (isEmpty()) {
        printf("Stack is empty\n");
    } else {
        printf("Top element is %d\n", stack[top]);
    }
}

// Display operation (traverse stack from top to bottom)
void display() {
    if (isEmpty()) {
        printf("Stack is empty\n");
    } else {
        printf("Stack elements (top to bottom): ");
        for (int i = top; i >= 0; i--) {
            printf("%d ", stack[i]);
        }
        printf("\n");
    }
}

int main() {
    push(10);
    push(20);
    push(30);
    display();

    peek();
    pop();
    display();
    peek();

    // test isFull() and isEmpty()
    if (isFull())
        printf("Stack is full now\n");
    else
        printf("Stack is not full\n");

    if (isEmpty())
        printf("Stack is empty now\n");
    else
        printf("Stack is not empty\n");

    return 0;
}
