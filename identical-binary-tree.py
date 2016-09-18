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
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        if a == b == None:
            return True
        elif a is not None and b is not None:
            if a.val == b.val:
                return self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right)
            return False
        else:
            return False
