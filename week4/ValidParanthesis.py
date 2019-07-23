class Solution:
    def isValid(self, s: str) -> bool:
        # Time - O(n)
        # Space - O(n)
        stack = []  # To store opened paranthesis
        for elem in s:
            if elem in {'(', '[', '{'}:  # if opened paranthesis, add it to stack
                stack.append(elem)
            else:  # if closed and stack is empty, return False
                if len(stack) == 0:
                    return False
                # Check if last element of stack is a matching open paranthesis.
                if elem == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif elem == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif elem == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        if len(stack) == 0:
            return True
        return False