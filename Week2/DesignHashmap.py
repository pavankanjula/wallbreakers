class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Used Seperate chaining to handle collisions.
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [None] * 1000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        h_val = self._hash(key)  # calculates hash value.
        if self.map[
            h_val] is None:  # if the space at hashed value in array is free, we will put there.Otherwise, we will attach as a chain next to it.
            self.map[h_val] = Node(key, value)
        else:
            cur = self.map[h_val]
            while cur.next is not None:
                if cur.key == key:
                    cur.value = value
                    return
                cur = cur.next
            if cur.key == key:
                cur.value = value
            else:
                cur.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        h_val = self._hash(key)
        if self.map[
            h_val] is None:  # if the element at hashed valus index in array is free, then there is no such key in the hashmap and we return -1
            return -1
        else:  # Otherwise, we check in that chain and will return the corresponding value
            cur = self.map[h_val]
            while cur.next is not None:
                if cur.key == key:
                    return cur.value
                cur = cur.next
            if cur.key == key:
                return cur.value
            else:
                return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        h_val = self._hash(key)
        if self.map[h_val] is None:
            return
        else:
            if self.map[h_val].key == key:
                self.map[h_val] = self.map[h_val].next
            else:
                cur = self.map[h_val]
                while cur.next is not None:
                    if cur.next.key == key:
                        cur.next = cur.next.next
                        return
                    cur = cur.next

    def _hash(self, key):
        return key % 1000