# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        elif root.left is None:
            return self.postorderTraversal(root.right) + [root.val] 
        elif root.right is None:
            return self.postorderTraversal(root.left) + [root.val] 
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]