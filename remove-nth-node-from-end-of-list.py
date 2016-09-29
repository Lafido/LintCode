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
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        if head and n > 0:
            dummy = ListNode(0)
            dummy.next = head
            p, q = dummy, dummy
            cnt = 0
            while cnt < n and p:
                p = p.next
                cnt += 1

            if cnt == n:
                while p.next:
                    p = p.next
                    q = q.next
                if q.next:
                    q.next = q.next.next
            return dummy.next

