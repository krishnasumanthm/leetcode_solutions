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
        stack1 = [root]
        result = []
        stack2 = []
        while len(stack1) != 0:
            current = stack1.pop()
            stack2.append(current)
            if current.left is not None:
                stack1.append(current.left)
            if current.right is not None:
                stack1.append(current.right)
        while len(stack2) != 0:
            result.append(stack2.pop().val)
        
        return result