class Solution(object):
    def calPoints(self, ops):
        #Time - O(n)
        #Space - O(n)
        stack = [] #A stack to add points after each round
        for elem in ops: #Loop through the given list
            if elem == 'C': #if 'C', removes last valid round points
                if len(stack) > 0:
                    stack.pop()
            elif elem == 'D': # if 'D', if we have valid rounds before, double the most recent valid round points
                if len(stack) > 0:
                    stack.append(2* stack[-1])
            elif elem == '+': # If '+', check if 2 valid rounds were present and add them as the current round points.
                if len(stack) > 1:
                    stack.append(stack[-1] + stack[-2])
                elif len(stack) > 0:
                    stack.append(stack[-1])
            else:
                stack.append(int(elem))
        return sum(stack) #Finally return the sum of points  of all the rounds