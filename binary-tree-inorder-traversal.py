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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        if not root:
            return []
        else:
            left = self.inorderTraversal(root.left)
            right = self.inorderTraversal(root.right)
            left.append(root.val)
            left.extend(right)
            return left