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
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        else:
            left = self.preorderTraversal(root.left)
            right = self.preorderTraversal(root.right)
            ret = [root.val]
            ret.extend(left)
            ret.extend(right)
            return ret

