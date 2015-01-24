# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    
    def reorderList(self, head):
        if head is None or head.next is None:
            return head
            
        temp_list = []
        current = head
        while current is not None:
            temp_list.append(current)
            current = current.next
        lt = len(temp_list)
        for i in xrange(lt // 2):
            temp_list[i].next = temp_list[lt-i-1]
            temp_list[lt-i-1].next = temp_list[i+1]
        temp_list[lt // 2].next = None
            
        return head
    