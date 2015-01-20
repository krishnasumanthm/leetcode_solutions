# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        ptr1 = head
        ptr2 = head
        for i in xrange(n-1):
            ptr2 = ptr2.next
        if ptr2.next == None:
            head = head.next
        else:
            ptr2 = ptr2.next
            while ptr2.next != None:
                ptr2 = ptr2.next
                ptr1 = ptr1.next
            ptr1.next = ptr1.next.next
        return head
        
                
        
        
        
        