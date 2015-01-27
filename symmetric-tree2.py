# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        q = [[root.left, root.right]]
        while len(q) != 0:
            temp1, temp2 = q.pop(0)
            if not (temp1 or temp2):
                continue 
            elif (temp1 and temp2) and temp1.val == temp2.val:
                q.append([temp1.left, temp2.right])
                q.append([temp1.right, temp2.left])
            else:   
                return False
        return True