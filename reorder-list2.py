# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    
    def reorderList(self, head):
        if head is None or head.next is None or head.next.next is None:
            return head
            
        ptr1 = head
        ptr2 = head
        while ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        
        current  = ptr1
        prev = None
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        node = head
        
        while prev.next is not None :
            temp1 = node.next
            temp2 = prev.next
            node.next = prev
            prev.next = temp1
            node = temp1
            prev = temp2
        return head