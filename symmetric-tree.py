# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def temp_Symmetric(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.temp_Symmetric(left.left, right.right) and self.temp_Symmetric(left.right, right.left)
    
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.temp_Symmetric(root.left, root.right)
        
            
        