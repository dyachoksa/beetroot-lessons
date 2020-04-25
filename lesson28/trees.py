class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def __repr__(self):
        return f"<Node value={self.value} children={self.children}>"

    def print_tree(self, level=0):
        print(
            " " * 4 * level,
            "\U0001F341" if not self.children else "\U0001F332",
            self.value,
        )
        for item in self.children:
            item.print_tree(level + 1)

    def add(self, node):
        self.children.append(node)


tree = Node("Root")

tree.add(Node("Child 1"))

node = Node("Sub-tree 1")
node.add(Node("Child 2"))
tree.add(node)

node = Node("Sub-tree 2")
node.add(Node("Child 3"))
node.add(Node("Child 4"))

tree.add(node)

# print(tree)

tree.print_tree()
