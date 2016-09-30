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
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """
    def reverse(self, head):
        if head:
            dummy = ListNode(0)
            dummy.next = None
            p, q = head, dummy
            while p:
                temp = dummy.next
                dummy.next = p
                p = p.next
                dummy.next.next = temp
            return dummy.next