# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        new_head = head.next
        remaining_part = head.next.next
        head.next.next = head
        head.next = self.swapPairs(remaining_part)
        
        return new_head