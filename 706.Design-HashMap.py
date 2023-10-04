class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    def __init__(self):
        self.data = [ListNode() for _ in range(10_000)]

    def hash(self, key):
        return hash(key) % len(self.data)

    def put(self, key: int, value: int) -> None:
        h = self.hash(key)
        curr = self.data[h]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        h = self.hash(key)
        curr = self.data[h]

        while curr:
            if curr.key == key:
                return curr.val
            else:
                curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        curr = self.data[h]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
            else:
                curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
