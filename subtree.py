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
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        # write your code here
        if not T2:
            return True
        elif not T1:
            return False
        return self.isIdentical(T1, T2) or self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)

    def isIdentical(self, a, b):
        # Write your code here
        if not a and not b:
            return True
        elif not a or not b:
            return False
        if a.val != b.val:
            return False
        return self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right)