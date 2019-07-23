class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        #Time - O(n)
        #Space - O(n)
        stack = [0] #Tracks the depth of the current bracket
        for char in S:
            if char is '(': #At every open bracket, we will treat as new and appends 0
                stack.append(0)
            else: #At close bracket, we will calculate the value according to the rule and add to the previuos value.
                last = stack.pop()
                stack[-1] += max(2*last, 1)
        return stack[-1]