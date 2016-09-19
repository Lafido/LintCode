"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        if root:
            left = root.left
            root.left = root.right
            root.right = left
            if root.left:
                self.invertBinaryTree(root.left)
            if root.right:
                self.invertBinaryTree(root.right)
