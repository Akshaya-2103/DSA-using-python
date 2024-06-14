class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        node = Node(data)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        else:
            return self.front.data

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

queue = Queue()
print(queue.is_empty()) 

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.size()) 

print("Front of the queue: ",queue.peek())  
print("Dequeue: ",queue.dequeue())  
print("Dequeue: ",queue.dequeue())  
print("Dequeue: ",queue.dequeue()) 
print(queue.is_empty())