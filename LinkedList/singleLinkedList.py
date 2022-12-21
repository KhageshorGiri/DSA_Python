
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
        print("constructor is created for class single linked list.")    

    # method for inserting the new node at the beginning of the linked list.
    def insertAtBeginning(self, data):
        pass

    # method for inserting the new node at the end of the linked list.
    def insertAtEnd(self, data):
        pass

    # method for inserting the new node at the given position of the linked list.
    def insertAtPosition(self, position, data):
        pass

    # method for deleting the node form the beginning of the linked list
    def deleteFroBeginning(self):
        pass

    # method for deleting the node form end of the linked list
    def deleteFromEnd(self):
        pass

    # method for deleting the node form givin position of the linked list
    def deleteFromPosition(self, position):
        pass

    # method for printing the all elements of the linked list.
    def printAllElements(self):
        pass

    # method to find the length of the linked list
    def lengthOfList(self):
        pass


# code execution starts here
if __name__ == "__main__":
    singleLinkedList = SingleLinkedList()