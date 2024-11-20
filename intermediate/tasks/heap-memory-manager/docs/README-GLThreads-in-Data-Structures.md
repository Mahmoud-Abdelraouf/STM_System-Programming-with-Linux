## README: GLThreads in Data Structures

### Table of Contents

1. [Introduction](#introduction)
2. [Why It's Called GLThreads](#why-its-called-glthreads)
3. [Key Concepts](#key-concepts)
4. [Advantages](#advantages)
5. [Use Cases](#use-cases)
6. [Implementation of Fundamental Data Structures Using GLThreads](#implementation-of-fundamental-data-structures-using-glthreads)
   - [1. Linked List with GLThreads](#1-linked-list-with-glthreads)
   - [2. Queue with GLThreads](#2-queue-with-glthreads)
   - [3. Binary Tree with GLThreads](#3-binary-tree-with-glthreads)
7. [Advanced GLThreads Examples](#advanced-glthreads-examples)
   - [1. Double-Ended Queue (Deque) with GLThreads](#1-double-ended-queue-deque-with-glthreads)
   - [2. Circular Linked List with GLThreads](#2-circular-linked-list-with-glthreads)
8. [Comparison: Traditional vs. GLThreads Implementation](#comparison-traditional-vs-glthreads-implementation)
9. [Conclusion](#conclusion)
10. [References](#references)

### Introduction

**GLThreads** (Generic Linked Threads) is a powerful programming technique used to manage data structures with enhanced flexibility and memory efficiency. GLThreads allow data structures to embed nodes directly within them, making it possible for a single data structure to participate in multiple linked structures simultaneously. This technique is particularly useful in low-level systems programming, where performance and memory efficiency are critical.

### Why It's Called GLThreads

The term **GLThreads** or **Generic Linked Threads** originates from the concept of "threads" in the context of linked lists and data structures. In traditional computing, a thread refers to a sequence of execution, often in the context of threading and concurrency. However, in the context of GLThreads:

- **"Thread"** is used metaphorically to represent the "thread of connections" that link elements together in a data structure. Just as a thread in sewing connects fabric pieces together, in GLThreads, the embedded nodes connect elements within data structures, creating a "thread" of linked elements.
- The **"Linked"** part of GLThreads emphasizes that these threads are specifically about linking data elements within a structure, allowing the data structure to participate in multiple linked lists or other structures simultaneously.

- **Generic** indicates that this technique is not limited to any specific type of data structure (such as linked lists) but can be applied to various structures, including queues, trees, and more.

### Key Concepts

- **Embedded Nodes**: Instead of using standalone nodes with pointers to the next and previous elements, GLThreads embed these nodes directly within the data structure. This allows the structure to be part of multiple lists without modification.

- **Offset-Based Navigation**: Pointers to next and previous nodes are calculated using offsets within the containing structure. This allows for flexible management of data structures.

- **Multiple List Participation**: A single data structure can participate in multiple lists, queues, or other linked structures simultaneously, enabling more complex relationships between data elements.

### Advantages

1. **Memory Efficiency**: By embedding nodes within the data structure, GLThreads reduce memory overhead by avoiding separate allocations for each node.
2. **Flexibility**: The same data structure can be linked into multiple lists or queues without needing to modify its definition.

3. **Improved Cache Performance**: Since nodes are embedded within a structure that is often accessed together, cache locality is improved.

### Use Cases

- **Operating Systems**: Managing processes or tasks in different queues (e.g., run queue, wait queue) simultaneously.
- **Embedded Systems**: Efficiently managing resources with minimal overhead.
- **Complex Data Management**: Any system where the same data structure needs to participate in multiple lists or other linked structures.

### Implementation of Fundamental Data Structures Using GLThreads

#### 1. **Linked List with GLThreads**

```c
#include <stddef.h>
#include <stdio.h>

typedef struct glthread_node {
    struct glthread_node *prev;
    struct glthread_node *next;
} glthread_node_t;

typedef struct {
    char name[32];
    int id;
    glthread_node_t glnode;
} employee_t;

#define OFFSET_OF(type, member) ((size_t)&(((type *)0)->member))
#define GLTHREAD_TO_STRUCT(ptr, type, member) \
    (type *)((char *)(ptr) - OFFSET_OF(type, member))

void glthread_add_next(glthread_node_t *base_node, glthread_node_t *new_node) {
    new_node->prev = base_node;
    new_node->next = base_node->next;
    if (base_node->next) {
        base_node->next->prev = new_node;
    }
    base_node->next = new_node;
}

void init_glthread(glthread_node_t *glnode) {
    glnode->prev = NULL;
    glnode->next = NULL;
}

int main() {
    employee_t e1 = {.name = "Alice", .id = 1};
    employee_t e2 = {.name = "Bob", .id = 2};

    init_glthread(&e1.glnode);
    init_glthread(&e2.glnode);

    glthread_add_next(&e1.glnode, &e2.glnode);

    glthread_node_t *head = &e1.glnode;
    while (head) {
        employee_t *emp = GLTHREAD_TO_STRUCT(head, employee_t, glnode);
        printf("Employee: %s, ID: %d\n", emp->name, emp->id);
        head = head->next;
    }

    return 0;
}
```

#### 2. **Queue with GLThreads**

```c
typedef struct glthread_queue {
    glthread_node_t *front;
    glthread_node_t *rear;
} glthread_queue_t;

void enqueue(glthread_queue_t *queue, glthread_node_t *new_node) {
    if (queue->rear == NULL) {
        queue->front = new_node;
        queue->rear = new_node;
    } else {
        glthread_add_next(queue->rear, new_node);
        queue->rear = new_node;
    }
}

glthread_node_t *dequeue(glthread_queue_t *queue) {
    if (queue->front == NULL) {
        return NULL;
    }
    glthread_node_t *front_node = queue->front;
    queue->front = front_node->next;
    if (queue->front == NULL) {
        queue->rear = NULL;
    }
    return front_node;
}

int main() {
    employee_t e1 = {.name = "Alice", .id = 1};
    employee_t e2 = {.name = "Bob", .id = 2};

    init_glthread(&e1.glnode);
    init_glthread(&e2.glnode);

    glthread_queue_t queue = {0};

    enqueue(&queue, &e1.glnode);
    enqueue(&queue, &e2.glnode);

    glthread_node_t *node;
    while ((node = dequeue(&queue)) != NULL) {
        employee_t *emp = GLTHREAD_TO_STRUCT(node, employee_t, glnode);
        printf("Dequeued Employee: %s, ID: %d\n", emp->name, emp->id);
    }

    return 0;
}
```

#### 3. **Binary Tree with GLThreads**

```c
typedef struct glthread_tree_node {
    glthread_node_t left_node;
    glthread_node_t right_node;
} glthread_tree_node_t;

typedef struct {
    char name[32];
    int id;
    glthread_tree_node_t gltree_node;
} tree_employee_t;

void add_left_child(tree_employee_t *parent, tree_employee_t *child) {
    glthread_add_next(&parent->gltree_node.left_node, &child->gltree_node.left_node);
}

void add_right_child(tree_employee_t *parent, tree_employee_t *child) {
    glthread_add_next(&parent->gltree_node.right_node, &child->gltree_node.right_node);
}

int main() {
    tree_employee_t root = {.name = "CEO", .id = 1};
    tree_employee_t left = {.name = "Manager", .id = 2};
    tree_employee_t right = {.name = "CTO", .id = 3};

    init_glthread(&root.gltree_node.left_node);
    init_glthread(&root.gltree_node.right_node);
    init_glthread(&left.gltree_node.left_node);
    init_glthread(&right.gltree_node.right_node);

    add_left_child(&root, &left);
    add_right_child(&root, &right);

    printf("Root: %s, Left: %s, Right: %s\n", root.name, left.name, right.name);

    return 0;
}
```

### Advanced GLThreads Examples

#### 1. **Double-Ended Queue (Deque) with GLThreads**

```c
typedef struct glthread_deque {
    glthread_node_t *front;
    glthread_node_t *rear;
} glthread_deque_t;

void deque_add_front(glthread_deque_t *deque, glthread_node_t *new_node) {
    if (deque->front == NULL) {
        deque->front = new_node;
        deque->rear = new_node;
    } else {
        glthread_add_next(new_node, deque->front);
        deque->front = new_node;
    }
}

void deque_add_rear(glthread_deque_t *deque, glthread_node_t *new_node) {
    if (deque->rear == NULL) {
        deque->front = new_node;
        deque->rear = new_node;
    } else {
        glthread_add_next(deque->rear, new_node);
        deque->rear = new_node;
    }
}

glthread_node_t *deque_remove_front(glthread_deque_t *deque) {
    if (deque->front == NULL) {
        return NULL;
    }
    glthread_node_t *front_node = deque->front;
    deque->front = front_node->next;
    if (deque->front == NULL) {
        deque->rear = NULL;
    }
    return front_node;
}

glthread_node_t *deque_remove_rear(glthread_deque_t *deque) {
    if (deque->rear == NULL) {
        return NULL;
    }
    glthread_node_t *rear_node = deque->rear;
    deque->rear = rear_node->prev;
    if (deque->rear == NULL) {
        deque->front = NULL;
    }
    return rear_node;
}

int main() {
    employee_t e1 = {.name = "Alice", .id = 1};
    employee_t e2 = {.name = "Bob", .id = 2};

    init_glthread(&e1.glnode);
    init_glthread(&e2.glnode);

    glthread_deque_t deque = {0};

    deque_add_front(&deque, &e1.glnode);
    deque_add_rear(&deque, &e2.glnode);

    glthread_node_t *node;

    node = deque_remove_front(&deque);
    employee_t *emp = GLTHREAD_TO_STRUCT(node, employee_t, glnode);
    printf("Dequeued from front: %s, ID: %d\n", emp->name, emp->id);

    node = deque_remove_rear(&deque);
    emp = GLTHREAD_TO_STRUCT(node, employee_t, glnode);
    printf("Dequeued from rear: %s, ID: %d\n", emp->name, emp->id);

    return 0;
}
```

#### 2. **Circular Linked List with GLThreads**

```c
void glthread_add_circular(glthread_node_t *base_node, glthread_node_t *new_node) {
    glthread_add_next(base_node, new_node);
    new_node->next = base_node;
    base_node->prev = new_node;
}

int main() {
    employee_t e1 = {.name = "Alice", .id = 1};
    employee_t e2 = {.name = "Bob", .id = 2};
    employee_t e3 = {.name = "Charlie", .id = 3};

    init_glthread(&e1.glnode);
    init_glthread(&e2.glnode);
    init_glthread(&e3.glnode);

    glthread_add_circular(&e1.glnode, &e2.glnode);
    glthread_add_circular(&e2.glnode, &e3.glnode);

    glthread_node_t *current = &e1.glnode;
    for (int i = 0; i < 6; i++) { // Iterate more than the list size to show circularity
        employee_t *emp = GLTHREAD_TO_STRUCT(current, employee_t, glnode);
        printf("Employee: %s, ID: %d\n", emp->name, emp->id);
        current = current->next;
    }

    return 0;
}
```

### Comparison: Traditional vs. GLThreads Implementation

#### Traditional Linked List Implementation

In a traditional linked list, each node is typically a standalone structure containing pointers to the next (and possibly previous) nodes, along with the data. For example:

```c
typedef struct node {
    struct node *next;
    int data;
} node_t;

node_t *create_node(int data) {
    node_t *new_node = (node_t *)malloc(sizeof(node_t));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

void append(node_t **head, int data) {
    node_t *new_node = create_node(data);
    if (*head == NULL) {
        *head = new_node;
        return;
    }
    node_t *current = *head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = new_node;
}
```

**Explanation:**

- In the traditional approach, each node is an independent entity that needs to be dynamically allocated.
- It is less flexible when it comes to using the same data structure in multiple lists, and managing memory efficiently requires careful handling.

#### GLThreads Implementation

In the GLThreads approach, the node is embedded within the data structure itself, and offset-based calculations are used to navigate the links:

```c
typedef struct {
    char name[32];
    int id;
    glthread_node_t glnode;
} employee_t;

// Functions like glthread_add_next and others as defined earlier
```

**Explanation:**

- **Memory Efficiency:** No need for separate memory allocations for nodes; they are embedded within the structure.
- **Flexibility:** The same structure can be part of multiple lists or other data structures simultaneously.
- **Cache Performance:** Better cache locality because related data is stored contiguously.

### Conclusion

GLThreads provide a flexible and memory-efficient way to manage complex data structures, particularly in systems where performance and memory use are critical. By embedding linkage nodes directly within the data structures and using offset-based navigation, GLThreads allow the same data structure to be part of multiple linked structures without additional overhead.

### References

1. **Linux Kernel Documentation**: Explore how similar concepts are implemented in the Linux kernel, particularly in managing processes and other kernel objects.
2. **GLib Documentation**: Learn about `GList` and other data structures in GLib, which can be adapted to follow GLThread-like patterns.
3. **Advanced Data Structures Books**: Books like "The Art of Computer Programming" by Donald Knuth provide deep insights into data structures and their implementation.
