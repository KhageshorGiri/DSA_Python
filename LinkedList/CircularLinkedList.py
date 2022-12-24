

# Creating a class for Node
class Node:
    def __init__(self):
        self.data = None
        self.next = None
    # method for setting the data field of the node
    def setData(self, info):
        self.data = info
    #method for getting the data field of the node
    def getData(self):
        return self.data
    #method for setting the next field of the node
    def setNext(self, nextNode):
        self.next = nextNode
    #method for getting the next filed of the node
    def getNext(self):
        return self.next
    #returns true if the node points to another node
    def hasNext(self):
        return self.next != None

# creating  a class for a circular linked list.
class CircularLinkedList:
    def __init__(self):
        self.first = None
        self.last = None    

    # method for inserting the new node at the beginning of the linked list.
    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.first == None:
            newNode.setNext(newNode)
            self.first = newNode
            self.last = newNode
        else:
            newNode.setNext(self.first)
            self.first = newNode
            self.last.setNext(newNode)

    # method for inserting the new node at the end of the linked list.
    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.first == None:
            self.first = newNode
            self.last = newNode
            newNode.setNext(self.first)
        else:
            self.last.setNext(newNode)
            self.last = newNode
            newNode.setNext(self.first)

    # method for inserting the new node at the given position of the linked list.
    def insertAtPosition(self, position, data):
        newNode = Node()
        newNode.setData(data)
        if self.first == None:
            self.first = newNode
            self.last = newNode
            self.last.setNext(newNode)
        else:
            temp = self.first
            for i in range(1, position-1):
                temp = temp.getNext()
            newNode.setNext(temp.getNext())
            temp.setNext(newNode)
            del temp

    # method for deleting the node form the beginning of the linked list
    def deleteFroBeginning(self):       
        if self.first == None:
            print("Nothing to Delete.\nThe list this Empty.")
        elif self.first == self.last:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = temp.getNext()
            self.last.setNext(self.first)
            del temp

    # method for deleting the node form end of the linked list
    def deleteFromEnd(self):
        if self.first == None:
            print("Nothing to Delete.\nThe list this Empty.")
        elif self.first == self.last:
            self.first = None
            self.last = None
        else:
            temp = self.first
            while temp.getNext() != self.last:
                temp = temp.getNext()
            temp.setNext(self.first)
            self.last = temp
            del temp

    # method for deleting the node form givin position of the linked list
    def deleteFromPosition(self, position):
        if self.first == None:
            print("Nothing to Delete.\nThe list this Empty.")
        elif self.first == self.last:
            self.first = None
            self.last = None
        else:
            temp = self.first
            for i in range(1, position-1):
                temp = temp.getNext()
            hold = temp.getNext()
            temp.setNext(hold.getNext())
            del temp, hold

    # method for printing the all elements of the linked list.
    def printAllElements(self):
        temp = self.first
        if temp == None:
            print("Nothing to Print.\nLinked List is Empty")
        while temp:
            print(temp.getData())
            temp = temp.getNext()
            if temp == self.first:
                break
        del temp

    # method to find the length of the linked list
    def lengthOfList(self):
        count = 0
        temp = self.first
        while temp:
            count += 1
            temp = temp.getNext()
            if temp == self.first:
                break
        print("The length is {0}".format(count))       
        del temp

# code execution starts here
if __name__ == "__main__":
    circularLinkedList = CircularLinkedList()
    
    # inserting at the beginning
    # circularLinkedList.insertAtBeginning(3)
    # circularLinkedList.insertAtBeginning(2)
    # circularLinkedList.insertAtBeginning(1)

    # inserting at the beginning
    # circularLinkedList.insertAtEnd(3)
    # circularLinkedList.insertAtEnd(2)
    # circularLinkedList.insertAtEnd(1)

    # inserting at the given position
    # circularLinkedList.insertAtEnd(3)
    # circularLinkedList.insertAtEnd(2)
    # circularLinkedList.insertAtEnd(1)
    # circularLinkedList.insertAtPosition(2, 4)

    # deleting form beginning
    # circularLinkedList.insertAtEnd(3)
    # circularLinkedList.insertAtEnd(2)
    # circularLinkedList.insertAtEnd(1)
    # print("Before Deleting.")
    # circularLinkedList.printAllElements()
    # circularLinkedList.deleteFroBeginning()
    # print("After Deleting form First.")

    # deleting form end
    circularLinkedList.insertAtEnd(3)
    circularLinkedList.insertAtEnd(2)
    circularLinkedList.insertAtEnd(1)
    print("Before Deleting.")
    circularLinkedList.printAllElements()
    circularLinkedList.deleteFromEnd()
    print("After Deleting form First.")

    # deleting form given position
    # circularLinkedList.insertAtEnd(3)
    # circularLinkedList.insertAtEnd(2)
    # circularLinkedList.insertAtEnd(1)
    # print("Before Deleting.")
    # circularLinkedList.printAllElements()
    # circularLinkedList.deleteFromPosition(2)
    # print("After Deleting form First.")


    #printing the length of linked list
    circularLinkedList.lengthOfList()
    # printing all the elements of liked list
    circularLinkedList.printAllElements()
    
