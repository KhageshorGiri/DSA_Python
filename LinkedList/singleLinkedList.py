import sys

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

# creating  a class for a single linked list.
class SingleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    # method for inserting the new node at the beginning of the linked list.
    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.first == None:
            self.first = newNode
            self.last = newNode
        else:
            newNode.setNext(self.first)
            self.first = newNode

    # method for inserting the new node at the end of the linked list.
    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.first == None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.setNext(newNode)
            self.last = newNode

    # method for inserting the new node at the given position of the linked list.
    def insertAtPosition(self, position, data):
        newNode = Node()
        newNode.setData(data)
        if self.first == None:
            self.first = newNode
            self.last = newNode
        else:
            temp = self.first
            for i in range(1, position-1):
                temp = temp.getNext()
            newNode.setNext(temp.getNext())
            temp.setNext(newNode)

    # method for deleting the node form the beginning of the linked list
    def deleteFroBeginning(self):
        temp = self.first
        if temp == None:
            print("Void Deletion.\nLinked List is Empty.")
            return
        else:
            temp = self.first
            self.first =  temp.getNext()
        del temp

    # method for deleting the node form end of the linked list
    def deleteFromEnd(self):
        temp = self.first
        if self.first == None:
            print("Void Deletion.\nLinked List is Empty.")
            return
        elif self.first.getNext() == None:
            self.first = None
        else:
            while temp.getNext().getNext() != None:
                temp = temp.getNext()
            temp.setNext(None)
        del temp

    # method for deleting the node form givin position of the linked list
    def deleteFromPosition(self, position):
        temp = self.first
        if self.first == None:
            print("Void Deletion.\nLinked List is Empty.")
            return
        else:
            for i in range(1, position-1):
                temp = temp.getNext()
            hold = temp.getNext()
            temp.setNext(hold.getNext())
        del temp, hold

    # method for printing the all elements of the linked list.
    def printAllElements(self):
        temp = self.first
        if temp == None:
            print("The Linked List is Empty.")
        else:
            while temp != None:
                print(temp.getData())
                temp = temp.getNext()
        del temp

    # method to find the length of the linked list
    def lengthOfList(self):
        count = 0
        temp = self.first
        while temp != None:
            count += 1
            temp = temp.getNext()
        del temp
        print("The Length of our linked list is {0}".format(count))


# code execution starts here
if __name__ == "__main__":
    singleLinkedList = SingleLinkedList()
    
    # inserting at the beginning
    singleLinkedList.insertAtBeginning(3)
    singleLinkedList.insertAtBeginning(2)
    singleLinkedList.insertAtBeginning(1)

    # inserting at the beginning
    # singleLinkedList.insertAtEnd(3)
    # singleLinkedList.insertAtEnd(2)
    # singleLinkedList.insertAtEnd(1)

    # inserting at the given position
    # singleLinkedList.insertAtEnd(3)
    # singleLinkedList.insertAtEnd(2)
    # singleLinkedList.insertAtEnd(1)
    # singleLinkedList.insertAtPosition(2, 4)

    # deleting form beginning
    # singleLinkedList.insertAtEnd(3)
    # singleLinkedList.insertAtEnd(2)
    # singleLinkedList.insertAtEnd(1)
    # print("Before Deleting.")
    # singleLinkedList.printAllElements()
    # singleLinkedList.deleteFroBeginning()
    # print("After Deleting form First.")

    # deleting form end
    # singleLinkedList.insertAtEnd(3)
    # singleLinkedList.insertAtEnd(2)
    # singleLinkedList.insertAtEnd(1)
    # print("Before Deleting.")
    # singleLinkedList.printAllElements()
    # singleLinkedList.deleteFromEnd()
    # print("After Deleting form First.")

    # deleting form given position
    # singleLinkedList.insertAtEnd(3)
    # singleLinkedList.insertAtEnd(2)
    # singleLinkedList.insertAtEnd(1)
    # print("Before Deleting.")
    # singleLinkedList.printAllElements()
    # singleLinkedList.deleteFromPosition(2)
    # print("After Deleting form First.")


    #printing the length of linked list
    singleLinkedList.lengthOfList()
    # printing all the elements of liked list
    singleLinkedList.printAllElements()
    
