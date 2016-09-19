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
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        p = head
        p_list_1 = l1
        p_list_2 = l2
        while p_list_1 and p_list_2:
            if p_list_1.val < p_list_2.val:
                p.next = p_list_1
                p_list_1 = p_list_1.next
                p = p.next
            elif p_list_1.val >= p_list_2.val:
                p.next = p_list_2
                p_list_2 = p_list_2.next
                p = p.next
        if p_list_1:
            p.next = p_list_1
        if p_list_2:
            p.next = p_list_2
        return head.next
