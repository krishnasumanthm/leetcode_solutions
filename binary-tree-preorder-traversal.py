# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        result = []
        while len(stack) != 0:
            current = stack.pop()
            result.append(current.val)
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)
        return result