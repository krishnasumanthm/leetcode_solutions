# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getLength(self, head):
        current = head
        length = 0
        while current != None:
            current = current.next
            length +=1
        return length
        
    def getIntersectionNode(self, headA, headB):
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)

        if lenA > lenB:
            lenA, lenB   = lenB, lenA
            headA, headB = headB, headA
        
        if lenA == 0 or lenB == 0:      
            return None
            
        currentA = headA
        currentB = headB
        for i in xrange(lenB - lenA):
            currentB = currentB.next
        
        while currentA != None and id(currentA) != id(currentB):
            currentA = currentA.next
            currentB = currentB.next
        
        return currentA