# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        new_list_head = ListNode(0)
        temp = new_list_head
        while l1 is not None and l2 is not None:
            if l1.val<=l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        while l1 is not None:
            temp.next = l1
            l1 = l1.next
            temp = temp.next
        while l2 is not None:
            temp.next = l2
            l2 = l2.next
            temp = temp.next
        return new_list_head.next
            