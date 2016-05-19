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

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        if root is None:
            return None
        result = []
        node_queue = [root]
        while len(node_queue) != 0:
            node = node_queue.pop(0)
            if node is not None:
                result.append(str(node.val))
                left_child = node.left
                right_child = node.right
                node_queue.append(left_child)
                node_queue.append(right_child)
            else:
                result.append('#')

        while result[-1] == '#' and len(result) > 1:
            result.pop(-1)
        return result

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    '''
    def deserialize(self, data):
        if data is None or len(data) == 0:
            return None
        root = TreeNode('#')
        if len(data) > 0:
            root.val = data.pop(0)
            node_queue = [root]
            data_len = len(data)
            while data_len > 0 and len(node_queue) > 0:
                if data_len > 1:
                    parent = node_queue.pop(0)
                    left_child_val = data.pop(0)
                    if left_child_val != '#':
                        left_child = TreeNode(left_child_val)
                        parent.left = left_child
                        node_queue.append(left_child)
                    else:
                        parent.left = None

                    right_child_val = data.pop(0)
                    if right_child_val != '#':
                        right_child = TreeNode(right_child_val)
                        parent.right = right_child
                        node_queue.append(right_child)
                    else:
                        parent.right = None
                elif data_len == 1:
                    parent = node_queue.pop(0)
                    left_child_val = data.pop(0)
                    if left_child_val != '#':
                        left_child = TreeNode(left_child_val)
                        parent.left = left_child
                        node_queue.append(left_child)
                    else:
                        parent.left = None

                    parent.right = None
                data_len = len(data)

            while len(node_queue) > 0:
                node = node_queue.pop(0)
                node.left = None
                node.right = None

        return root

if __name__ == "__main__":
    sol = Solution()
    parent = TreeNode('1')
    left_child = TreeNode('2')
    right_child = TreeNode('3')
    parent.left = left_child
    parent.right = right_child
    left_child.left = None
    left_child.right = None

    right_left_child = TreeNode('4')
    right_right_child = TreeNode('15')
    right_child.left = right_left_child
    right_child.right = right_right_child

    ser_str = sol.serialize(parent)
    print(ser_str)
    tree = sol.deserialize(ser_str)
    print(tree)