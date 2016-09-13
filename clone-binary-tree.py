"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """

    def cloneTree(self, root):
    # Write your code here
        if not root:
            return None
        else:
            left_tree = self.cloneTree(root.left)
            right_tree = self.cloneTree(root.right)
            cloned_root = TreeNode(root.val)
            cloned_root.left = left_tree
            cloned_root.right = right_tree
            return cloned_root