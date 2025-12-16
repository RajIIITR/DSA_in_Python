class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def traversal(self):
        temp = self
        while temp is not None:
            print(temp.data, end="")
            if temp.next is not None:
                print("->", end="")
            temp = temp.next
        print()

    def insert(self, data, position):
        temp = self

        if position == 0:
            new_node = Node(data)
            new_node.next = self.next
            self.next = new_node
            return

        while temp.next is not None and position > 1:
            temp = temp.next
            position -= 1

        if position == 1:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
        else:
            print("Invalid position")

    def delete(self, position):
        # Case 1: Delete head
        if position == 0:
            return self.next   # new head

        temp = self
        count = 0

        # Move to node just before the target
        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1

        # Invalid position
        if temp is None or temp.next is None:
            print("Invalid position")
            return self

        # Delete node
        curr = temp.next
        temp.next = curr.next
        curr.next = None
        del curr

        return self


if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)

    head.insert(25, 2)   # Insert after 20
    head.traversal()

    head = head.delete(2)   # Delete first node
    head.traversal()