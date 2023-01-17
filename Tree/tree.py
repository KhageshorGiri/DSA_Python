
class BasicTree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, childNode):
        childNode.parent = self
        self.children.append(childNode)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

if __name__ == "__main__":
    rootNode = BasicTree("Electronics")

    laptop = BasicTree("Laptop")
    laptop.add_child(BasicTree("Mac"))
    laptop.add_child(BasicTree("Dell"))
    laptop.add_child(BasicTree("Thinkpad"))

    mobile = BasicTree("Cell Phone")
    mobile.add_child(BasicTree("iPhone"))
    mobile.add_child(BasicTree("Mi"))
    mobile.add_child(BasicTree("Vivo"))

    tv = BasicTree("TV")
    tv.add_child(BasicTree("CG"))
    tv.add_child(BasicTree("LG"))

    rootNode.add_child(laptop)
    rootNode.add_child(mobile)
    rootNode.add_child(tv)

    rootNode.print_tree()