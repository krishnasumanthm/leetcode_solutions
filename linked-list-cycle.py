# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None:
            return False
        ptr1 = head
        ptr2 = head
        while(ptr1 is not None and ptr2 is not None and ptr2.next is not None):
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            if id(ptr1) == id(ptr2):
                return True
        else:
            return False