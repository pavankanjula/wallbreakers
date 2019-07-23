import collections
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = collections.deque()  # To use Queue methods append and popleft.
        self.last = -1094795586  # To track most recently added element.

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)  # Add to Queue
        self.last = x  # Update most recently added element

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.stack) == 0:
            return self.last
        if len(self.stack) == 1:  # if queue has only one element, just pop it and return.
            self.last = -1094795586
            return self.stack.popleft()
        # we will create a temporary deque to hold all element we pop from deque until the length reaches 2.
        temp = collections.deque()
        while len(self.stack) > 2:
            temp.append(self.stack.popleft())
        # Once length 2 is reached, we pop one element and store as cur_last. This will be set as self.last after popping.
        cur_last = self.stack.popleft()
        self.last = cur_last
        temp.append(cur_last)
        # to_return takes last element
        to_return = self.stack.popleft()
        self.stack = temp  # assign the temporary deque to original deque
        return to_return  # Return the last element

    def top(self) -> int:
        """
        Get the top element.
        """
        # simply return self.last as we are updating it each time we pop and push.
        return self.last

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.stack):
            return False
        return True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()