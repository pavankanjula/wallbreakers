# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        # Time - O(n) Traverse through n nodes
        # Space - O(n) for recursive call stack
        self.longest = 0  # Tracks longest path with same values
        self.helper(root)  # calls helper function
        return self.longest

    def helper(self, node):
        if node is None:
            return 0
        left_path = self.helper(node.left)  # longest univalpath of left subtree
        right_path = self.helper(node.right)  # longest univalpath of right subtree
        left_sub = right_sub = 0
        if node.left and node.val == node.left.val:  # if left node value is equal to current node value, then add one
            left_sub = 1 + left_path
        if node.right and node.val == node.right.val:
            right_sub = 1 + right_path
        self.longest = max(self.longest, left_sub + right_sub)  # update the longest property
        return max(left_sub, right_sub)  # Take the subtree with the longest to build the path