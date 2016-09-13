# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        p = head
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return head


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(5)
    next = ListNode(6)
    next_next = ListNode(6)
    head.next = next
    head.next.next = next_next
    sol.removeElements(head, 6)
    while head:
        print(head.val, "-> ", end="")
        head = head.next
    print("Null")
