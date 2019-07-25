# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # Time - O(n) #Traverse through each node.
        # Space - O(n) for the recursive call stack
        if root is None:
            return 0
        return self.helper(root, 0, None)

    def helper(self, node, sum, parent=None):
        if node.left is None and node.right is None:
            if parent is None:  # if reached root from leaf
                return sum
            if parent.left is node:  # if current leaf is left leaf, add it to sum
                return sum + node.val
            else:
                return sum
        elif node.left is None:  # add the sum of left leaves of right subtree
            return sum + self.helper(node.right, sum, node)
        elif node.right is None:  # add the sum of left leaves of left subtree
            return sum + self.helper(node.left, sum, node)
        else:  # If both subtrees are there, add from both
            return sum + self.helper(node.right, sum, node) + self.helper(node.left, sum, node)