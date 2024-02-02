class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(int(val))
        newNode.next = self.head
        self.head = newNode
        if self.tail is None:
            self.tail = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(int(val))
        if self.tail is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            temp = current.next
            current.next = Node(int(val))
            current.next.next = temp
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next

        self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)