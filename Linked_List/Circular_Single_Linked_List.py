class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def traversal(self):
        if self is None:
            return
        temp = self.next
        print (self.data, end="->")
        while temp is not self:
            print(temp.data, end="->")
            temp = temp.next
        print()

    def insert(self, data, position):
        new_node = Node(data)

        n = 1
        temp = self
        while temp.next != self:
            temp = temp.next
            n += 1

        position = position % n

        if position == 0:
            new_node.next = self
            temp.next = new_node   
            return new_node      

        temp = self
        for _ in range(position - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        return self
    
    def delete(self, position):
        n = 1
        temp = self
        while temp.next != self:
            temp = temp.next
            n += 1

        position = position % n

        if position == 0:
            temp = self
            while temp.next != self:
                temp = temp.next
            temp.next = self.next
            self = self.next
            return self

        temp = self
        for _ in range(position - 1):
            temp = temp.next

        temp.next = temp.next.next
        return self



if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = head

    head.traversal()

    head = head.insert(25, 2)
    head.traversal()

    head = head.delete(3)
    head.traversal()