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
        while q:
            temp = q.pop(0)
            if not (temp[0] or temp[1]):
                continue
            elif (temp[0] and temp[1]) and temp[0].val == temp[1].val:
                q.append([temp[0].left, temp[1].right])
                q.append([temp[0].right, temp[1].left])
            else:   
                return False
        return True
            