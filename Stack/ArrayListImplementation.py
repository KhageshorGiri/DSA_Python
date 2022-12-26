
class StackUsingDynamicArray:
    def __init__(self, limit=10):
        self.stack = limit*[None]
        self.limit = limit

    # method to insert element into stack
    def push(self, data):
        if self.isFull():
            self.reSize()
        self.stack.append(data)

    # method to delete element form stack
    def pop(self):
        if self.isEmpty():
            print("Stack UnderFlow")
            return
        else:
            return self.stack.pop()

    # method to check whether a stack is empty or not
    def isEmpty(self):
        return len(self.stack) <= 0

    # method to check whether a stack is full or not
    def isFull(self):
        return len(self.stack) >= self.limit

    # method to get the top element of stack
    def peek(self):
        return self.stack[-1]

    # method to resize the stack
    def reSize(self):
        newStack = list(self.stack)
        self.limit = 2*limit
        self.stack = newStack

    # method to print stack
    def display(self):
        print("Stack Elements:")
        print(self.stack)



if __name__ == "__main__":
    stk = StackUsingDynamicArray(2)
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.display()
    deletedItem = stk.pop()
    stk.display()