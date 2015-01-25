# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    
    def get_length(self, head):
        lt = 0
        current = head
        while current is not None:
            current = current.next
            lt += 1
        return lt
        
    def reverseKGroup(self, head, k):
        if head is None:
            return head
        count = 0
        n_groups = self.get_length(head) // k
        if n_groups == 0:
            return head
        if k == 1:
            return head
            
        count = 1
        current = head
        prev = None
        while count <= k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1
        
        rem_part = next_node
        temp = prev
        while temp.next is not None:
            temp = temp.next
        temp.next = self.reverseKGroup(rem_part,k)
        
        return prev  