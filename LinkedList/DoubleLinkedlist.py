
# create a Node type data structure for doubled linked list
class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None
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
    #method for setting the previous field of the node
    def setPrev(self, pervNode):
        self.prev = pervNode
    #method for getting the previous node of the current node
    def getPrev(self):
        return self.prev
    # returns true if the nodes have any previous node
    def hasPrev(self):
        return self.prev != None


# creating  a class for a doubled linked list.
class DoubledLinkedList:
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
            self.first.setPrev(newNode)
            self.first = newNode

    # method for inserting the new node at the end of the linked list.
    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.first == None:
            self.first = newNode
            self.last = newNode
        else:
            newNode.setPrev(self.last)
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
            for i in range(1, position):
                temp = temp.getNext()
            newNode.setPrev(temp)
            newNode.setNext(temp.getNext())
            temp.setNext(newNode)
            del temp

    # method for deleting the node form the beginning of the linked list
    def deleteFroBeginning(self):
        if self.first == None:
            print("Nothing to Delete.")
        else:
            temp = self.first
            self.first = temp.getNext()
            del temp

    # method for deleting the node form end of the linked list
    def deleteFromEnd(self):
        if self.first == None:
            print("Nothing to Delete.")
        else:
            temp = self.first
            while temp.getNext().getNext() != None:
                temp = temp.getNext()
            temp.setNext(None)
            self.last = temp
            del temp

    # method for deleting the node form givin position of the linked list
    def deleteFromPosition(self, position):
        if self.first == None:
            print("Nothing to Delete.")
        else:
            temp = self.first
            for i in range(1, position):
                temp = temp.getNext()
            hold = temp.getNext()
            temp.setNext(hold.getNext())
            hold.setNext(temp)
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
    doubledLinkedList = DoubledLinkedList()
    
    # inserting at the beginning
    doubledLinkedList.insertAtBeginning(3)
    doubledLinkedList.insertAtBeginning(2)
    doubledLinkedList.insertAtBeginning(1)

    # inserting at the beginning
    # doubledLinkedList.insertAtEnd(3)
    # doubledLinkedList.insertAtEnd(2)
    # doubledLinkedList.insertAtEnd(1)

    # inserting at the given position
    # doubledLinkedList.insertAtEnd(3)
    # doubledLinkedList.insertAtEnd(2)
    # doubledLinkedList.insertAtEnd(1)
    # doubledLinkedList.insertAtPosition(2, 4)

    # deleting form beginning
    # doubledLinkedList.insertAtEnd(3)
    # doubledLinkedList.insertAtEnd(2)
    # doubledLinkedList.insertAtEnd(1)
    # print("Before Deleting.")
    # doubledLinkedList.printAllElements()
    # doubledLinkedList.deleteFroBeginning()
    # print("After Deleting form First.")

    # deleting form end
    # doubledLinkedList.insertAtEnd(3)
    # doubledLinkedList.insertAtEnd(2)
    # doubledLinkedList.insertAtEnd(1)
    # print("Before Deleting.")
    # doubledLinkedList.printAllElements()
    # doubledLinkedList.deleteFromEnd()
    # print("After Deleting form First.")

    # deleting form given position
    # doubledLinkedList.insertAtEnd(3)
    # doubledLinkedList.insertAtEnd(2)
    # doubledLinkedList.insertAtEnd(1)
    # print("Before Deleting.")
    # doubledLinkedList.printAllElements()
    # doubledLinkedList.deleteFromPosition(2)
    # print("After Deleting form First.")


    #printing the length of linked list
    doubledLinkedList.lengthOfList()
    # printing all the elements of liked list
    doubledLinkedList.printAllElements()