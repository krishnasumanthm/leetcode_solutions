class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        sum = ListNode(0)
        temp = sum
        while l1 is not None or l2 is not None or carry:
            temp.val = carry
            if l1:
                temp.val = temp.val + l1.val
                l1 = l1.next
            if l2:
                temp.val  = temp.val + l2.val
                l2 = l2.next
            carry = temp.val / 10
            temp.val = temp.val % 10
            if l1 or l2 or carry:
                temp.next = ListNode(0)
                temp = temp.next
        return sum