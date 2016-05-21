"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        result = []

        def searchRangeHelper(root):
            if not root:
                return
            if root.val > k1:
                searchRangeHelper(root.left)
            if k1 <= root.val <= k2:
                result.append(root.val)
            if root.val < k2:
                searchRangeHelper(root.right)
        searchRangeHelper(root)
        return result
