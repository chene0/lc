# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = None
        curr = head
        nxt = head.next

        while nxt is not None:
            new_nxt = nxt.next

            curr.next = prev
            nxt.next = curr

            prev = curr
            curr = nxt
            nxt = new_nxt

        return curr
