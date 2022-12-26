
class StackUsingArray:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = 10

    # method to push/insert item in stack
    def push(self, data):
        if self.isFull():
            print("Stack Overflow")
            return
        else:
            self.stack.append(data)

    # method to pop/delete data form stack
    def pop(self):
        if self.isEmpty():
            print("Stack UnderFlow")
            return
        else:
            return self.stack.pop()

    # method to check if stack is empty or not
    def isEmpty(self):
        return len(self.stack) <= 0
    
    # method to check if stack is full or not
    def isFull(self):
        return len(self.stack) >= self.limit

    # method to peek/see top element of stack
    def peek(self):
        if self.isEmpty():
            print('Stack UnderFlow')
            return
        else:
            return self.stack[-1]

    # method to print all element of stack
    def display(self):
        print("Elements of stack;")
        print(self.stack)


if __name__ == "__main__":
    stk = StackUsingArray()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.display()
    deletedItem = stk.pop()
    stk.display()