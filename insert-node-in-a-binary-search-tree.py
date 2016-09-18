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
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if not root:
            return node
        else:
            p = root
            while True:
                if node.val < p.val:
                    if p.left:
                        p = p.left
                    else:
                        p.left = node
                        break
                else:
                    if p.right:
                        p = p.right
                    else:
                        p.right = node
                        break
            return root
