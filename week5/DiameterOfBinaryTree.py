# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # Time - O(n) Traverse through all the nodes once
        # Space - O(n) for the recursive call stack
        if root is None:
            return 0
        self.longest = float(
            '-inf')  # At every node with two chidren it stores the longest pth including the current node in the path
        root_include_longest = self.helper(
            root)  # Considers only longest one from two chidren and construct the path upwards.
        return max(root_include_longest, self.longest)

    def helper(self, node):
        # 4 cases in total
        if node.left is None and node.right is None:  # case 1 - return 0 at lef nodes
            return 0
        elif node.left is None:  # case 2 - if only right node present, directly add it upwards
            return 1 + self.helper(node.right)
        elif node.right is None:  # case 3 - if only left node present, directly add it upwards
            return 1 + self.helper(node.left)
        else:  # case 4 - if both nodes present, we need check if the path from left to right including the current node is longest and update it.
            left_path = self.helper(node.left)
            right_path = self.helper(node.right)
            self.longest = max(self.longest, 2 + left_path + right_path)
            # Then take the longest of left and right to add upwards
            return max(1 + left_path, 1 + right_path)