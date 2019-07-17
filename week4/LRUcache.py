class Node:
    def __init__(self, key, value):
        self.prev = None
        self.key = key
        self.value = value
        self.next = None


class LRUCache:
    # To do the given type of operations in O(1), we used a hashmap and Doubly linked list.
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashmap = {}
        self.head = Node("head", "head")  # To track head pointer
        self.tail = Node("tail", 'tail')  # To track tail pointer
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # Time - O(1)
        if key in self.hashmap:
            cur = self.hashmap[key]
            self.remove(cur)
            self.insert(cur)
            return cur.value
        return -1

    def put(self, key: int, value: int) -> None:
        # Time - O(1)
        # if a node with given key is present in hashmap, we update the value of that node with new value.
        # Remove from it's current position and add to the head.
        if key in self.hashmap:
            cur = self.hashmap[key]
            cur.value = value
            self.remove(cur)
            self.insert(cur)
        # If not present we look for the current size of hashmap.
        else:
            self.hashmap[key] = Node(key, value)
            # If current size is less than capacity, we can safely add the node and increase the size by 1
            if self.size < self.capacity:
                cur = self.hashmap[key]
                self.insert(cur)
                self.size += 1
            # If maximum capicity is reached, we should remove the least recently used node and add the new one
            else:
                least = self.tail.prev
                self.remove(least)
                del self.hashmap[least.key]
                cur = self.hashmap[key]
                self.insert(cur)

    def insert(self, cur):
        # inserts a given node at the head position.
        head = self.head
        headnext = self.head.next
        head.next = cur
        headnext.prev = cur
        cur.prev = head
        cur.next = headnext

    def remove(self, cur):
        # Removes a given node from the linked list.
        prev = cur.prev
        next = cur.next
        prev.next = next
        next.prev = prev
