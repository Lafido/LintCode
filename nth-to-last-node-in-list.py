"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list.
    """
    def nthToLast(self, head, n):
        if head:
            p = head
            q = head
            count = 0
            while p:
                p = p.next
                count += 1
                if count > n:
                    q = q.next
            return q