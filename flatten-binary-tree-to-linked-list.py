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
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here
        if not root:
            return None
        else:
            right_child = root.right
            left_child = root.left
            root.left = None
            root.right = self.flatten(left_child)
            p = root
            while p.right:
                p = p.right
            p.right = self.flatten(right_child)
            return root

