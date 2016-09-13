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
    """
       @param root: The root of binary tree.
       @return: True if this Binary tree is Balanced, or false.
       """

    def isBalanced(self, root):
        # write your code here
        if root is None:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(
            self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1

    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
