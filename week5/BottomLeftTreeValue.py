# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # Time - O(n) Traverse through n nodes
        # Space - O(n) for recursive call stack
        self.row = 0  # Tracks the maximum row number
        self.ans = None  # stores and updates answer if we go to new row
        self.helper(root, 1)
        return self.ans

    def helper(self, node, cur_row):
        if node is None:
            return
        if cur_row > self.row:  # Whenever we go to new row, updates answer with first element of that row
            self.ans = node.val
            self.row = cur_row  # updates self.row with current row number as well.
        self.helper(node.left, cur_row + 1)
        self.helper(node.right, cur_row + 1)