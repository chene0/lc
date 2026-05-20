# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        tort = head

        while hare and hare.next:
            tort = tort.next
            hare = hare.next.next

            if tort == hare:
                return True

        return False
