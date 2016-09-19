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
    @return: An integer
    """
    def maxDepth(self, root):
        if root:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            max_depth = left_depth if left_depth > right_depth else right_depth
            return max_depth + 1
        else:
            return 0