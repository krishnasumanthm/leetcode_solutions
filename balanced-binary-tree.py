# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def get_height(self, root):
        if root is None:
            return 0
        return 1+max(self.get_height(root.left), self.get_height(root.right))
    
    def isBalanced(self, root):
        if root is None:
            return True
        rh = self.get_height(root.right)
        lh = self.get_height(root.left)
        if abs(rh-lh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
            