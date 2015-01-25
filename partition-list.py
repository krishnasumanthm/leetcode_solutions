# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        temp_list1 = ListNode(0)
        temp_list2 = ListNode(0)
        temp1 = temp_list1
        temp2 = temp_list2
        while head is not None:
            if head.val < x:
                temp1.next = head
                temp1 = temp1.next
            else:
                temp2.next = head
                temp2 = temp2.next
            head = head.next
        
        temp1.next = temp_list2.next
        temp2.next = None
        return temp_list1.next