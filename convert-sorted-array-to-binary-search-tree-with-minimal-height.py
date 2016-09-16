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
    @param A: a list of integer
    @return: a tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here
        if A:
            size = len(A)
            if size == 1:
                return TreeNode(A[0])
            else:
                half = size // 2
                tree_node = TreeNode(A[half])
                tree_node.left = self.sortedArrayToBST(A[:half])
                tree_node.right = self.sortedArrayToBST(A[half+1:])
                return tree_node
        else:
            return None

