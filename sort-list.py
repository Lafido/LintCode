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
    def sortList(self, head):
        result = self.mergSort(head)
        return result

    def mergSort(self, head):
        if not head or not head.next:
            return head
        left, right = self.split(head)
        L1 = self.mergSort(left)
        L2 = self.mergSort(right)
        return self.merge(L1, L2)

    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        p = ListNode(0)
        head = p
        while left and right:
            if left.val < right.val:
                head.next = left
                left = left.next
                head = head.next
            else:
                head.next = right
                right = right.next
                head = head.next
        if left:
            head.next = left
        elif right:
            head.next = right
        else:
            head.next = None
        return p.next

    def split(self, head):
        slow = head
        fast = head
        prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return head, slow
