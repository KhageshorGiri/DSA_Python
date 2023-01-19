
# Operations on Binary Binary Tree
# 1. Insert a new Node
# 2. Search a node
# 3. Travese the tree
# 4. Delete a node form the tree.

# The tree is 
        #             27
        #     14              35
        # 10      19      31      42


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # insert new node in binary tree
    def insert(self, data):
        if self.data:
            if self.data > data:
                # insert node into left side.
                if self.left is None:
                    self.left = BinaryTreeNode(data)
                else:
                    self.left.insert(data)
            else:
                # insert node into right side.
                if self.right is None:
                    self.right = BinaryTreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # print binary tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data)
        if self.right:
            self.right.PrintTree()

    # Traversing a Binary Tree

    # 1. in-order Traversing
    #   Left --> Node --> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
        # if root:
        #     self.inorderTraversal(root.left)
        #     print(root.data)
        #     self.inorderTraversal(root.right)

    # 2. pre-order Traversing
    #    Node --> Left --> Right
    def preorderTraverse(self, root):
        if root:
            print(root.data)
            self.preorderTraverse(root.left)
            self.preorderTraverse(root.right)

    # 3. post-order Traversing
    #    Left --> Right --> Node
    def postorderTraverse(self, root):
        if root:
            self.postorderTraverse(root.left)
            self.postorderTraverse(root.right)
            print(root.data)


if __name__ == "__main__":
    root = BinaryTreeNode(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    #root.PrintTree()
    print("Inorder Traversing a Binary Tree.\n" + "-"*20)
    print(root.inorderTraversal(root))
    print("Pre-Order Traversing a Binary Tree.\n" + "-"*20)
    root.preorderTraverse(root)
    print("Post-Order Traversing a Binary Tree.\n" + "-"*20)
    root.postorderTraverse(root)



