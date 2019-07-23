class MyQueue:

    def __init__(self):
        # Time - O(n)
        # Space - O(n)
        """
        Initialize your data structure here.
        """
        self.queue = []  # Using list with pop and append methods(Like stack)
        self.first = float('inf')  # Tracks the first element.

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # add element to the stack
        self.queue.append(x)
        if len(self.queue) == 1:  # if stack has no elements, this is the first one.
            self.first = x

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.queue) == 0:
            return
        if len(self.queue) == 1:
            self.first = float('inf')
            return self.queue.pop()
        temp = []  # A temporary array to transfer all the elements from the stack.
        while len(
                self.queue) > 2:  # if last 2 elements are left, we will make the first one as self.first and pop the other one out. Now, transfer all the elements back to self.queue
            temp.append(self.queue.pop())
        temp_first = self.queue.pop()
        self.first = temp_first
        to_return = self.queue.pop()
        self.queue.append(temp_first)
        while len(temp):
            self.queue.append(temp.pop())
        return to_return

    def peek(self) -> int:
        """
        Get the front element.
        """
        # As we are tracking first element, we can return it directly.
        return self.first

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if len(self.queue) else True