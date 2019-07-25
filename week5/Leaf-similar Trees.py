# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Time - O(n)
        # Space - O(n)
        seq1 = []  # List to hold all the leaf node values of first tree
        seq2 = []  # List to hold all the leaf node values of second tree
        self.leafs(root1, seq1)
        self.leafs(root2, seq2)
        # Now we compare the both lists and return True if same else False.
        if len(seq1) != len(seq2):
            return False
        else:
            for i in range(len(seq1)):
                if seq1[i] != seq2[i]:
                    return False
        return True

    def leafs(self, node, out):
        if node is None:
            return
        if node.left is None and node.right is None:
            # This is leaf node and append it to the seq list
            out.append(node.val)
            return
        if node.left:
            self.leafs(node.left, out)
        if node.right:
            self.leafs(node.right, out)
