# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    
    def reverse(self,head):
        current = head
        prev = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
            
    def reverseBetween(self, head, m, n):
        if head is None or head.next is None:
            return head
        if m == n:
            return head
            
        if m == 1:
            ptr1 = head
        else:
            current1 = head
            for i in xrange(m-2):
                current1 = current1.next
            ptr1 = current1.next
            
        ptr2 = head
        for i in xrange(n-1):
            ptr2 = ptr2.next
        
        current1 = head
        if current1 == ptr1:
            rem_part = ptr2.next
            ptr2.next = None
            temp_head = self.reverse(ptr1)
            temp1 = temp_head
            while temp1.next is not None:
                temp1 = temp1.next
            temp1.next = rem_part
            return temp_head
        else:
            while current1.next != ptr1:
                current1 = current1.next
            rem_part = ptr2.next
            ptr2.next = None
            temp1 = self.reverse(ptr1)
            current1.next = temp1
            while temp1.next is not None:
                temp1 = temp1.next
            temp1.next = rem_part
            return head