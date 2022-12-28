
class CircularQueue:
    # constructor
    def __init__(self, size):
        self.size = size
        # initializing queue with none
        self.queue = size*[None]
        self.front = -1
        self.rare = -1

    # method to check whether a queue is empty or not
    def isEmpty(self):
        return self.front == -1 and self.rare == -1

    # method to check whether a queue is full or not
    def isFull(self):
        return (self.rare + 1) % self.size == self.front

    # method to insert data in queue
    def Enqueue(self, data):
        if self.isFull():
            print("Queue is full")
            return
        elif(self.front == -1 and self.rare == -1):
            self.front = 0
            self.rare = 0
            self.queue[self.rare] = data
        else:
            self.rare = (self.rare + 1) % self.size
            self.queue[self.rare] = data

    # method to delete data from queue
    def Dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        elif (self.front == self.rare):
            temp = self.queue[self.front]
            self.front = self.rare = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return temp

    # method to peek element of queue
    def Front(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        else:
            return self.queue[self.front]

    # def method to display elements of queue
    def Display(self):
        if self.isEmpty():
            print("Queue UnderFlow")
            return
        else:
            print("Queue Elements:")
            print(self.queue)

if __name__ == "__main__":
    obj = CircularQueue(5)
    obj.Enqueue(1)
    obj.Enqueue(2)
    obj.Enqueue(3)
    obj.Enqueue(4)
    obj.Enqueue(5)

    print("Font:", obj.Front())
    obj.Display()

    print("Deleted Item:",obj.Dequeue())

    obj.Display()

    obj.Enqueue(6)
    obj.Display()
    