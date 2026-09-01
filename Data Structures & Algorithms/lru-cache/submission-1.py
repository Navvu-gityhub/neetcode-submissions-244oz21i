class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)    # LRU side
        self.right = Node(0, 0)   # MRU side

        # left <-> right
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        # Insert node just before right (MRU position)
        prev, nxt = self.right.prev, self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            # Move node to MRU position
            self.remove(node)
            self.insert(node)

            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        # If key already exists, remove old node
        if key in self.cache:
            self.remove(self.cache[key])

        # Create new node and insert as MRU
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # Evict LRU if capacity exceeded
        if len(self.cache) > self.capacity:
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]
