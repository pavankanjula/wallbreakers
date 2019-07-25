# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.helper(p, q)

    def helper(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False

        if node1.val != node2.val:
            return False
        else:
            return self.helper(node1.left, node2.left) and self.helper(node1.right, node2.right)
