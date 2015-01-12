# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return head
        temp_head = ListNode(0)
        temp_head.next = head
        current = temp_head
        while current.next:
            nextVal = current.next
            if nextVal.next and nextVal.val == nextVal.next.val:
                nextVal = nextVal.next
                while nextVal.next and nextVal.val == nextVal.next.val:
                    nextVal = nextVal.next
                current.next = nextVal.next
            else:
                current = current.next
        return temp_head.next
                    
            
            
       
                
                