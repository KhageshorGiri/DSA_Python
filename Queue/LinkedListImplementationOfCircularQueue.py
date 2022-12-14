
class Node:
    def __init__(self):
        self.data = None
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    # method to check whether a queue is empty or not
    def isEmpty(self):
        return self.first == None

    # method to insert element in queue
    def Enqueue(self, data):
        newNode = Node()
        newNode.data = data
        if self.isEmpty():
            self.first = newNode
            self.last = newNode
            self.last.next = self.first
        else:
            self.last.next = newNode
            self.last = newNode
            self.last.next = self.first

    # method to delete element for queue
    def Dequeue(self):
        if self.isEmpty():
            print("Queue UnderFlow")
            return
        elif self.first == self.last:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = temp.next
            self.last.next = self.first
            del temp

    # method to find the peek element of queue
    def peek(self):
        if self.isEmpty():
            print("Queue UnderFlow")
            return
        else:
            return self.first.data

    # method to display all element of queue
    def display(self):
        temp = self.first
        while temp != None:
            print(temp.data)
            temp = temp.next
            if temp == self.first:
                break
        del temp
if __name__ == "__main__":
    queue = Queue()
    #queue.Dequeue()
    #queue.peek()
    queue.Enqueue(1)
    queue.Enqueue(3)
    queue.Enqueue(5)
    queue.Enqueue(7)
    print("Queue Element")
    queue.display()
    print("Peek:", queue.peek())
    print("Popped Item:", queue.Dequeue())
    print("Queue Element")
    queue.display()