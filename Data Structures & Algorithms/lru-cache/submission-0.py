
class Node:
    def __init__ (self, key: int, val: int, prev: Node, next: Node):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1, None, None)
        self.tail = Node(-1, -1, None, self.head)
        self.head.prev = self.tail
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            # mend the spot where node used to be
            node.next.prev = node.prev
            node.prev.next = node.next

            # move node to the front of tail
            self.moveToEnd(node)
            return node.val

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            # mend the spot where node used to be
            node.next.prev = node.prev
            node.prev.next = node.next

            # move node to the front of tail
            self.moveToEnd(node)

        else:
            # create node and add to cache
            node = Node(key, value, None, None)
            self.cache[key] = node

            # move node to the front of tail
            self.moveToEnd(node)

            # if the cache is too big, evict top of head
            if len(self.cache) > self.capacity:
                evict_node = self.head.prev
                self.head.prev = evict_node.prev
                evict_node.prev.next = self.head
                del self.cache[evict_node.key]

    def moveToEnd(self, node: Node) -> None:
        # move node to the front of tail
        self.tail.next.prev = node
        node.next = self.tail.next
        node.prev = self.tail
        self.tail.next = node
