class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

    def __repr__(self):
        return f"<Node data={self.data} next={self.next}>"


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def remove(self):
        node = self.head
        self.head = node.next
        return node.data

    def search(self, value):
        node = None
        current = self.head

        while current is not None:
            if current.data == value:
                return current

            current = current.next

        return node

    def __repr__(self):
        current = self.head
        res = []
        while current is not None:
            res.append(current.data)
            current = current.next

        return " -> ".join(res)


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.add("d")
    linked_list.add("b")
    linked_list.add("f")

    print(repr(linked_list))

    el = linked_list.remove()
    print(linked_list)

    linked_list.add("a")
    linked_list.add("x")
    print(repr(linked_list))

    node = linked_list.search("b")
    print(repr(node))
