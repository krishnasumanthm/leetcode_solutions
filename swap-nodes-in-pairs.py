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
        current = head
        prev = None
        while current is not None and current.next is not None:
            if prev is not None:
                prev.next = current.next
            prev = current
            
            temp = current.next.next
            current.next.next = current
            current.next = temp
            current = current.next
        return new_head
        