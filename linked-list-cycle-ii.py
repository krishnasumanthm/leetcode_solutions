# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
            return None
        ptr1 = head
        ptr2 = head
        while(ptr1 is not None and ptr2 is not None and ptr2.next is not None):
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            if id(ptr1) == id(ptr2):
                break
        else:
            return None
        ptr3 = head
        ptr4 = ptr1
        while id(ptr3) != id(ptr4):
            ptr3 = ptr3.next
            ptr4 = ptr4.next
        return ptr3
            
         