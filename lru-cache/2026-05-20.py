class Node:
    def __init__(self, key, val, n=None, p=None):
        self.key = key
        self.val = val
        self.next = n
        self.prev = p


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.tail = Node(None, None)
        self.head = Node(None, None)

        self.tail.next = self.head
        self.head.prev = self.tail

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]

        # bubble up
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

        new_p = self.head.prev
        new_p.next = node
        node.next = self.head
        node.prev = new_p
        self.head.prev = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            p = self.head.prev
            node = Node(key, value, self.head, p)
            p.next = node
            self.head.prev = node
            self.map[key] = node

            if len(self.map) > self.capacity:
                self.map.pop(self.tail.next.key)

                new_n = self.tail.next.next
                new_n.prev = self.tail
                self.tail.next = new_n

            return

        node = self.map[key]
        node.val = value

        # bubble up
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

        new_p = self.head.prev
        new_p.next = node
        node.next = self.head
        node.prev = new_p
        self.head.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
