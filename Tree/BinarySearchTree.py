
# creating a node of binary search tree
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # method to insert new node in BST
    def insert(self, data):
        # if BST is empty, declare newNode as a root node.
        if self.data:
            # if newNode is greater then current node then insert into right side
            if self.data > data:
                if self.left is None:
                    self.left = BinarySearchTree(data)
                else:
                    self.left.insert(data)
            else:
                #insert into left side
                if self.right is None:
                    self.right = BinarySearchTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
  
    # print binary tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data, end= " ")
        if self.right:
            self.right.PrintTree()

    # get the maximum element of BST
    def get_minimum(self):
        if self == None:
            return None
        else:
            current = self
            while current.left != None:
                current = current.left
            return current


    # get the minimum element of BST
    def get_maximum(self):
        if self == None:
            return None
        else:
            current = self
            while current.right != None:
                current = current.right
            return current

    # search a particular element in BST
    def search(self, node):
        if node == self.data:
            return True
        if self.data > node:
            if self.left == None:
                return False
            else:
                return self.left.search(node)
        else:
            if self.right == None:
                return False
            else:
                return self.right.search(node)

    # Traversing a BST

    # in-order traverse
    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.data, end= " ")
            self.inorderTraversal(root.right)

    # pre-order Traversal
    def preorderTraverse(self, root):
        if root:
            print(root.data, end= " ")
            self.preorderTraverse(root.left)
            self.preorderTraverse(root.right)

    # post order Traversal
    def postorderTraverse(self, root):
        if root:
            self.postorderTraverse(root.left)
            self.postorderTraverse(root.right)
            print(root.data, end= " ")

    # delete a node from a BST
    def delete(self, key):
        # Base Case
        if self == None:
            return self
        # if the key is less then root then it lies in left sub-tree
        if self.data > key:
            self.left = self.left.delete(key)
        #if the key is greater then root then it lies in right sub-tree
        elif self.data < key:
            self.right = self.right.delete(key)
        else:
            # if root node is leaf node
            if self.left is None and self.right is None:
                return None
            
            # if node have only one children
            if self.left == None:
                temp = self.right
                del self
                return temp
            elif self.right == None:
                temp - self.left
                del self
                return temp
            
            # Node having 2 child
            # first of all get the in-order successor
            inorderSuccessor = self.right.get_minimum()

            # Copy the inorder successor's content to this node
            self.data = inorderSuccessor
            
            # delete the inorder successor
            self.right = self.right.delete(inorderSuccessor)

        return self


# Driver code
""" Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 """

if __name__ == "__main__":
    root = BinarySearchTree(None)
    root.insert(50)
    root.insert(70)
    root.insert(30)
    root.insert(40)
    root.insert(20)
    root.insert(60)
    root.insert(80)
    root.PrintTree()

    # print(f"The minimum element of tree is {root.get_minimum().data}")
    # print(f"The maximum element of tree is {root.get_maximum().data}") 

    # print("Searching Elements")
    # print(f"Searching For Node 30. {root.search(30)}")
    # print(f"Searching For Node 60. {root.search(60)}")
    # print(f"Searching For Node 100. {root.search(100)}")

    # print("Inorder Traversing a Binary Tree.\n" + "-"*20)
    # root.inorderTraversal(root)
    # print("Pre-Order Traversing a Binary Tree.\n" + "-"*20)
    # root.preorderTraverse(root)
    # print("Post-Order Traversing a Binary Tree.\n" + "-"*20)
    # root.postorderTraverse(root)

    # print("Inorder traversal of the given tree")
    # root.inorderTraversal(root)
    # print("\n\nDelete 20")
    # result = root.delete(20)
    # print("Inorder traversal of the modified tree")
    # root.inorderTraversal(result)
    
    # print("\n\nDelete 30")
    # result = root.delete(30)
    # print("Inorder traversal of the modified tree")
    # root.inorderTraversal(root)
    
    # print("\n\nDelete 50")
    # result = root.delete(50)
    # print("Inorder traversal of the modified tree")
    # root.inorderTraversal(root)
