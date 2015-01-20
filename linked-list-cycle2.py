# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None:
            return False
        flag = set()
        while head is not None:
            if id(head) in flag:
                return True
            else:
                flag.add(id(head))
            head = head.next
        else:
            return False