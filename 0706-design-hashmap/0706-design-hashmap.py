class Node:
    def __init__(self , val=-1, key=-1):
        self.val = val 
        self.key  = key
        self.next = None
class MyHashMap:

    def __init__(self):
        self.store = [Node()]*1000
    def put(self, key: int, value: int) -> None:
        dummy = self.store[key%1000]
        cur = dummy 

        while cur:
            if cur.key == key:
                cur.val = value
                break
            cur = cur.next
        else:
            newNode = Node(value , key)
            temp = dummy.next
            dummy.next = newNode 
            newNode.next = temp 
  
    def get(self, key: int) -> int:
        dummy = self.store[key%1000]
        cur = dummy 

        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next

        return -1

    def remove(self, key: int) -> None:
        dummy = self.store[key%1000]
        prev = dummy 
  
        while prev.next:
            if prev.next.key == key:
                prev.next = prev.next.next
                break
            prev = prev.next

        return 

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)