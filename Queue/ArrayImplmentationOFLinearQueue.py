
class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    # method to check whether a queue is empty or not
    def isEmpty(self):
        return len(self.queue) <= 0

    # method to check whether a queue is full or not
    def isFull(self):
        return len(self.queue) >= self.size

    # method to insert element in queue
    def Enqueue(self, data):
        if self.isFull():
            print("Queue Overflow.")
            return
        else:
            self.queue.append(data)

    # method to delete element form a queue
    def Dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return
        else:
            return self.queue.pop(0)

    # method to find peek element of queue
    def peek(self):
        if self.isEmpty():
            print("Queue Underflow")
            return
        else:
            return self.queue[0]

    # method to display all element of queue
    def display(self):
        print("Queue Elements:")
        print(self.queue)


if __name__ == "__main__":
    queue = Queue(5)
    #queue.Dequeue()
    queue.Enqueue(1)
    queue.Enqueue(2)
    queue.Enqueue(3)
    queue.Enqueue(4)
    print("Peek:", queue.peek())
    queue.display()
    print("Popped Item:", queue.Dequeue())
    queue.display()
 