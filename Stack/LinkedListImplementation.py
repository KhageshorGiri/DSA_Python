
class Node:
    def __init__(self):
        self.data = None
        self.next = None


class Stack:
    def __init__(self):
        self.first = None
        self.last = None

    # method to insert element into stack
    def push(self, data):
        newNode = Node()
        newNode.data = data
        if self.first == None:
            self.first = newNode
            self.last = newNode
        else:
            newNode.next = self.first
            self.first = newNode

    # method to delete element form stack
    def pop(self):
        if self.isEmpty():
            print("Stack UnderFlow")
            return
        else:
            temp = self.first
            self.first = self.first.next
            return temp.data

    # method to check whether a stack is empty or not
    def isEmpty(self):
        return self.first == None

    # method to get top element of stack
    def peek(self):
        if self.isEmpty():
            print("Stack UnderFlow")
            return
        else:
            return self.first.data

    # method to print all elements of stack
    def display(self):
        temp = self.first
        while temp != None:
            print(temp.data)
            temp = temp.next      


if __name__ == "__main__":
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.display()
    deletedItem = stk.pop()
    print("Deleted item", deletedItem)
    stk.display()