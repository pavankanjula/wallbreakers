class Node:

    def __init__(self, key):
        self.key = key
        self.next = None

#Used seperate chaining to handle collisions.
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = [None] * 10000

    def add(self, key: int) -> None:
        h_val = self._hash(key)
        cur = self.set[h_val]
        if self.set[h_val] is None: #if there is no key at the hashed value index, we will just add it there.
            self.set[h_val] = Node(key)
            return
        elif self.set[h_val].key == key: #if there is same key already, we will just return
            return
        while cur.next: #we traverse through the linkedlist and if we find same key, we will just return or else we add at the tail of the linked list.
            cur = cur.next
            if cur.key == key:
                return
        cur.next = Node(key)

    def remove(self, key: int) -> None:
        h_val = self._hash(key)
        if self.set[h_val] is None: # If the index at the hashed value is empty, we will return it.
            return
        elif self.set[h_val].key == key:
            self.set[h_val] = self.set[h_val].next
            return
        cur = self.set[h_val]
        while cur.next:
            if cur.next.key == key: #Traverse through the linkedlist and if we find the key, connect the previous node with the next node.
                cur.next = cur.next.next
                return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        h_val = self._hash(key)
        if self.set[h_val] is None: #if the hashed index is empty, return Flase
            return False
        else:
            cur = self.set[h_val]
            while cur: #Traverse through the linkedlist and if find the key, return True.
                if cur.key == key:
                    return True
                cur = cur.next
            return False #If while loop ends, we didn't find the key and return False.

    def _hash(self, num):
        return num % 10000