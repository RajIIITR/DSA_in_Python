class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
    
    def traversal(self):
        temp = self
        while temp is not None:
            print(temp.data, end = "->")
            temp = temp.next
        print()

    def insert(self, data, position):
        if position == 0:
            temp = Node(data)
            temp.next = self
            self.prev = temp
            self = temp
            return self
        else:
            temp = self
            count = 0
            while temp is not None and count < position-1:
                temp = temp.next
                count += 1
            
            if temp is None:
                print("Invalid Position")
                return self
            else:
                new_node = Node(data)
                new_node.next = temp.next
                new_node.prev = temp

                if temp.next is not None:  
                    temp.next.prev = new_node

                temp.next = new_node
                return self
            
    def delete(self, position):
        if position == 0:
            return self.next
        else:
            temp = self
            count = 0
            while temp is not None and count < position-1:
                temp = temp.next
                count += 1
            if temp is None and temp.next is None:
                print("Invalid Position")
                return self
            else:
                curr = temp.next
                temp.next = curr.next
                if curr.next is not None:
                    curr.next.prev = temp
                del curr
                return self
    
if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.prev = head
    head.next.next.prev = head.next

    head.traversal()

    head = head.insert(25, 3)
    head.traversal()

    head = head.delete(0)
    head.traversal()