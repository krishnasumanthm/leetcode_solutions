# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None:
            return head
            
        listLen = 0
        temp = head
        while temp != None:
            temp = temp.next
            listLen += 1
        
        k = k % listLen
        if k == 0:
            return head
        
        kth_node = head
        current = head
        for i  in xrange(k):
            current = current.next
        while current.next != None:
            current = current.next
            kth_node = kth_node.next
        current.next = head
        newHead = kth_node.next
        kth_node.next = None
        
        return newHead