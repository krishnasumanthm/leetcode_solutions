# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    res = None
    def findmax(self, root):
        if root == None:
            return 0
            
        max_l = self.findmax(root.left)
        max_r = self.findmax(root.right)
        if max_l < 0 and max_r < 0:
            self.res = max(self.res, root.val)
            return root.val
        if max_l > 0 and max_r > 0:
            self.res = max(self.res, root.val + max_r + max_l)
        
        temp_max = max(max_l, max_r) +root.val
        self.res = max(self.res, temp_max)
        return temp_max
    
    def maxPathSum(self, root):
        self.findmax(root)
        return self.res