class TreeNode:
    def __init__(self, name, position):
        self.data = name
        self.position = position
        self.children = []
        self.parent = None

    
    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def add_child(self, childNode):
        childNode.parent = self
        self.children.append(childNode)

    def print_tree(self, printOption):
        if printOption.lower() == "name":
            printValue = self.data
        elif printOption.lower() == "both":
            printValue = self.data + f"( {self.position} )"
        else:
            printValue = self.position

        spaces = " " * self.get_level() * 3
        perfix = spaces + "|--" if self.parent else ""
        print(perfix + printValue)
        for child in self.children:
            child.print_tree(printOption)

def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Shiva","Infrastructure Head")
    infra_head.add_child(TreeNode("Krishna","Cloud Manager"))
    infra_head.add_child(TreeNode("Bisnu", "App Manager"))

    cto = TreeNode("Ram", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Hanuman", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Indra","HR Head")

    hr_head.add_child(TreeNode("Laxman","Recruitment Manager"))
    hr_head.add_child(TreeNode("Bharat", "Policy Manager"))

    ceo = TreeNode("Karna", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

if __name__ == '__main__':
    rootNode = build_management_tree()
    rootNode.print_tree("Name")
    rootNode.print_tree("Post")
    rootNode.print_tree("Both")